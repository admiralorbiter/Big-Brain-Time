/* Requirement Clinic — Analysis & Review Engine */

(function(window) {
  'use strict';

  let reviewRules = [];
  let exercises = [];
  let currentRequirement = {
    statement: '',
    type: 'functional',
    source: '',
    rationale: '',
    structured: { trigger: '', actor: '', modal: 'shall', action: '', object: '', condition: '', outcome: '' },
    acceptance_criteria: [],
    findings: [],
    maturity: 'stated-requirement'
  };

  document.addEventListener('DOMContentLoaded', () => {
    loadData();
    initScreenNavigation();
    initEditorEvents();
  });

  function loadData() {
    Promise.all([
      fetch('content/rules.json').then(r => r.json()),
      fetch('content/exercises.json').then(r => r.json())
    ]).then(([rulesData, exercisesData]) => {
      reviewRules = rulesData;
      exercises = exercisesData;
      populateExerciseSelect();
      runAnalysis();
    }).catch(err => {
      console.warn('Could not load clinic JSON content:', err);
    });
  }

  function populateExerciseSelect() {
    const sel = document.getElementById('select-exercise');
    if (!sel || !exercises.length) return;
    sel.innerHTML = '<option value="">-- Choose a Guided Exercise --</option>' +
      exercises.map((ex, idx) => `<option value="${idx}">${ex.id}: ${ex.title} (${ex.domain})</option>`).join('');

    sel.addEventListener('change', (e) => {
      const idx = e.target.value;
      if (idx !== '') {
        loadExercise(exercises[idx]);
      }
    });
  }

  function loadExercise(ex) {
    document.getElementById('input-statement').value = ex.raw_requirement;
    document.getElementById('select-type').value = ex.type || 'functional';
    document.getElementById('input-source').value = ex.source || '';
    document.getElementById('input-rationale').value = ex.rationale || '';
    
    // Auto populate structured draft if improved statement exists
    document.getElementById('struct-outcome').value = ex.improved_statement || '';

    runAnalysis();
    switchScreen('screen-analyze');
  }

  function initScreenNavigation() {
    document.querySelectorAll('.tool-step-btn[data-screen]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const targetId = e.target.dataset.screen;
        switchScreen(targetId);
      });
    });
  }

  function switchScreen(screenId) {
    document.querySelectorAll('.clinic-screen').forEach(s => s.style.display = 'none');
    document.querySelectorAll('.tool-step-btn[data-screen]').forEach(b => b.classList.remove('active'));

    const targetScreen = document.getElementById(screenId);
    const targetBtn = document.querySelector(`.tool-step-btn[data-screen="${screenId}"]`);

    if (targetScreen) targetScreen.style.display = 'block';
    if (targetBtn) targetBtn.classList.add('active');

    if (screenId === 'screen-analyze') {
      runAnalysis();
    } else if (screenId === 'screen-structure') {
      updateStructuredPreview();
    } else if (screenId === 'screen-ac') {
      generateAcceptanceCriteria();
    } else if (screenId === 'screen-export') {
      updateExportSummary();
    }
  }

  function initEditorEvents() {
    const textarea = document.getElementById('input-statement');
    if (!textarea) return;

    textarea.addEventListener('input', () => {
      runAnalysis();
    });
  }

  function runAnalysis() {
    const text = (document.getElementById('input-statement')?.value || '').trim();
    currentRequirement.statement = text;
    currentRequirement.type = document.getElementById('select-type')?.value || 'functional';
    currentRequirement.source = document.getElementById('input-source')?.value || '';
    currentRequirement.rationale = document.getElementById('input-rationale')?.value || '';

    if (!text) {
      renderHighlightedText('');
      renderFindings([]);
      return;
    }

    const findings = [];
    reviewRules.forEach(rule => {
      try {
        const regex = new RegExp(rule.pattern, 'gi');
        let match;
        while ((match = regex.exec(text)) !== null) {
          findings.push({
            ruleId: rule.id,
            phrase: match[0],
            startIndex: match.index,
            endIndex: match.index + match[0].length,
            severity: rule.severity,
            message: rule.message,
            poor: rule.poor,
            improved: rule.improved,
            swebok_link: rule.swebok_link
          });
        }
      } catch(e) {}
    });

    currentRequirement.findings = findings;
    renderHighlightedText(text, findings);
    renderFindings(findings);
    updateMaturityState();
  }

  function renderHighlightedText(text, findings) {
    const container = document.getElementById('highlighted-text-surface');
    if (!container) return;

    if (!text) {
      container.innerHTML = '<span style="color: var(--text-dim); font-style: italic;">Paste or write a requirement on Screen 1 to begin analysis...</span>';
      return;
    }

    if (!findings || findings.length === 0) {
      container.innerHTML = `<p style="font-size: 1.05rem; line-height: 1.6;">${text}</p>
        <div style="margin-top: 12px; font-size: 0.85rem; color: #34d399;">✓ No automated review patterns triggered! Check structured criteria on Screen 3.</div>`;
      return;
    }

    // Sort findings by position
    const sorted = [...findings].sort((a,b) => a.startIndex - b.startIndex);
    let html = '';
    let lastIndex = 0;

    sorted.forEach((f, idx) => {
      if (f.startIndex >= lastIndex) {
        html += escapeHtml(text.substring(lastIndex, f.startIndex));
        const markClass = `flag-${f.severity}`;
        html += `<mark class="${markClass}" onclick="ClinicEngine.focusFinding(${idx})">${escapeHtml(f.phrase)}</mark>`;
        lastIndex = f.endIndex;
      }
    });
    html += escapeHtml(text.substring(lastIndex));

    container.innerHTML = `<p style="font-size: 1.05rem; line-height: 1.6;">${html}</p>`;
  }

  function renderFindings(findings) {
    const container = document.getElementById('findings-list-container');
    const countBadge = document.getElementById('finding-count-badge');
    if (!container) return;

    if (countBadge) countBadge.textContent = `${findings.length} Finding${findings.length === 1 ? '' : 's'}`;

    if (!findings || findings.length === 0) {
      container.innerHTML = '<p style="font-size: 0.85rem; color: var(--text-muted);">No review prompts triggered.</p>';
      return;
    }

    container.innerHTML = findings.map((f, idx) => `
      <div id="finding-card-${idx}" class="glass-card" style="padding: 14px; margin-bottom: 12px; border-left: 3px solid ${getSeverityColor(f.severity)};">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 4px;">
          <span style="font-size: 0.75rem; font-weight: 700; color: ${getSeverityColor(f.severity)}; text-transform: uppercase;">${f.severity} · ${f.phrase}</span>
          <a href="../../../ka/01-requirements/topics/${f.swebok_link}" target="_blank" style="font-size: 0.75rem; color: #06b6d4;">📖 SWEBOK Read →</a>
        </div>
        <p style="font-size: 0.88rem; color: var(--text-main); margin-bottom: 8px;">${f.message}</p>
        <details style="font-size: 0.82rem; color: var(--text-muted);">
          <summary style="cursor: pointer; color: var(--text-dim);">Compare Examples</summary>
          <div style="margin-top: 6px; padding: 6px; background: rgba(15,23,42,0.8); border-radius: 4px;">
            <div style="color: #fb7185;">🔴 ${f.poor}</div>
            <div style="color: #34d399; margin-top: 4px;">🟢 ${f.improved}</div>
          </div>
        </details>
      </div>
    `).join('');
  }

  function focusFinding(idx) {
    const el = document.getElementById(`finding-card-${idx}`);
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  function getSeverityColor(sev) {
    if (sev === 'high') return '#f43f5e';
    if (sev === 'medium') return '#f59e0b';
    return '#38bdf8';
  }

  function updateStructuredPreview() {
    const trig = document.getElementById('struct-trigger')?.value || '';
    const act = document.getElementById('struct-actor')?.value || 'the session-management system';
    const mod = document.getElementById('struct-modal')?.value || 'shall';
    const action = document.getElementById('struct-action')?.value || '';
    const cond = document.getElementById('struct-condition')?.value || '';
    const out = document.getElementById('struct-outcome')?.value || '';

    let res = '';
    if (trig) res += `WHEN ${trig}, `;
    res += `the ${act} ${mod} ${action} `;
    if (cond) res += `WHILE ${cond} `;
    if (out) res += `AND ${out}`;

    const previewEl = document.getElementById('structured-preview-text');
    if (previewEl) previewEl.textContent = res.trim() || currentRequirement.statement;
  }

  function generateAcceptanceCriteria() {
    const stmt = document.getElementById('structured-preview-text')?.textContent || currentRequirement.statement;
    const acContainer = document.getElementById('ac-list-container');
    if (!acContainer) return;

    const defaultAc = [
      `Given a completed session in an open reporting period`,
      `And the user has the Program Administrator role`,
      `When the user amends volunteer attendance`,
      `Then the updated attendance shall be saved`,
      `And an audit trail entry shall record previous and revised values.`
    ].join('\n');

    if (!acContainer.value) {
      acContainer.value = defaultAc;
    }
  }

  function updateMaturityState() {
    let state = 'stated-requirement';
    if (currentRequirement.statement.length > 20) state = 'analyzed-candidate';
    if (currentRequirement.source && currentRequirement.rationale) state = 'accepted-obligation';
    if (document.getElementById('ac-list-container')?.value) state = 'operationalized-ac';
    currentRequirement.maturity = state;
  }

  function updateExportSummary() {
    updateMaturityState();
    const badge = document.getElementById('export-maturity-badge');
    if (badge) badge.textContent = `Maturity State: ${currentRequirement.maturity.toUpperCase()}`;

    const mdPreview = document.getElementById('export-markdown-preview');
    if (mdPreview) {
      mdPreview.textContent = `# Requirement Record: REQ-${Date.now().toString().slice(-4)}
**Type:** ${currentRequirement.type}  
**Maturity State:** ${currentRequirement.maturity}  
**Source:** ${currentRequirement.source || 'Unspecified'}  

## Statement
${document.getElementById('structured-preview-text')?.textContent || currentRequirement.statement}

## Rationale
${currentRequirement.rationale || 'None provided.'}

## Acceptance Criteria
\`\`\`gherkin
${document.getElementById('ac-list-container')?.value || 'None defined.'}
\`\`\`
`;
    }
  }

  function saveToProject() {
    const proj = ProjectEngine.getActiveProject();
    const reqRecord = {
      id: `REQ-${Date.now().toString().slice(-4)}`,
      title: currentRequirement.statement.slice(0, 40) + '...',
      statement: document.getElementById('structured-preview-text')?.textContent || currentRequirement.statement,
      type: currentRequirement.type,
      source: currentRequirement.source,
      rationale: currentRequirement.rationale,
      priority: 'high',
      maturity: currentRequirement.maturity,
      acceptance_criteria: (document.getElementById('ac-list-container')?.value || '').split('\n'),
      swebok_links: ['3.1', '9.3']
    };

    proj.requirements = proj.requirements || [];
    proj.requirements.push(reqRecord);
    ProjectEngine.saveActiveProject(proj);
    alert(`Saved ${reqRecord.id} to project "${proj.project.name}"!`);
  }

  const SAMPLES = {
    'vague-staff': {
      statement: "The system should allow staff to quickly update a completed session.",
      type: "functional",
      source: "Program Operations",
      rationale: "Correct attendance and reporting mistakes"
    },
    'unmeasured-speed': {
      statement: "Staff shall receive session reports promptly.",
      type: "functional",
      source: "District Coordinator",
      rationale: "Verify monthly participation numbers"
    },
    'over-combined': {
      statement: "The system shall update attendance and notify volunteers and regenerate reports and update the audit log.",
      type: "functional",
      source: "Data Analytics Lead",
      rationale: "Keep downstream metrics synchronized"
    },
    'premature-tech': {
      statement: "Add a React dropdown button on the account screen to export CSV files.",
      type: "functional",
      source: "Branch Manager",
      rationale: "Enable offline transaction analysis"
    }
  };

  function injectSample(sampleKey) {
    const sample = SAMPLES[sampleKey];
    if (!sample) return;

    document.getElementById('input-statement').value = sample.statement;
    document.getElementById('select-type').value = sample.type;
    document.getElementById('input-source').value = sample.source;
    document.getElementById('input-rationale').value = sample.rationale;

    runAnalysis();
    switchScreen('screen-analyze');
  }

  function escapeHtml(str) {
    return str.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  }

  window.ClinicEngine = {
    focusFinding,
    updateStructuredPreview,
    saveToProject,
    injectSample
  };

})(window);
