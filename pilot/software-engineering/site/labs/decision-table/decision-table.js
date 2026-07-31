/* Decision Table Studio — Engine & Analysis */

(function(window) {
  'use strict';

  let currentTable = {
    title: 'Attendance Editing Permissions',
    conditions: [
      { name: "User Role", values: ["Program Administrator", "School Staff", "Volunteer"] },
      { name: "Session Status", values: ["Confirmed", "Completed", "Cancelled"] },
      { name: "Reporting Period", values: ["Open", "Locked"] }
    ],
    actions: [
      { name: "Allow Attendance Edit" },
      { name: "Require Correction Reason" },
      { name: "Record Audit History" },
      { name: "Reject Request" }
    ],
    rules: []
  };

  document.addEventListener('DOMContentLoaded', () => {
    loadData();
    initStudioEvents();
  });

  function loadData() {
    fetch('content/cases.json')
      .then(r => r.json())
      .then(cases => {
        populateCaseSelect(cases);
        generateRuleSpace();
      })
      .catch(e => {
        generateRuleSpace();
      });
  }

  function populateCaseSelect(cases) {
    const sel = document.getElementById('select-case');
    if (!sel || !cases) return;
    sel.innerHTML = '<option value="">-- Choose Example Case --</option>' +
      cases.map((c, idx) => `<option value="${idx}">${c.title} (${c.domain})</option>`).join('');

    sel.addEventListener('change', (e) => {
      const idx = e.target.value;
      if (idx !== '') {
        currentTable.title = cases[idx].title;
        currentTable.conditions = cases[idx].conditions;
        currentTable.actions = cases[idx].actions;
        currentTable.rules = [];
        renderConditions();
        renderActions();
        generateRuleSpace();
      }
    });
  }

  function initStudioEvents() {
    document.querySelectorAll('.tool-step-btn[data-studio-step]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        switchStep(e.target.dataset.studioStep);
      });
    });
  }

  function switchStep(stepId) {
    document.querySelectorAll('.studio-step').forEach(s => s.style.display = 'none');
    document.querySelectorAll('.tool-step-btn[data-studio-step]').forEach(b => b.classList.remove('active'));

    const targetStep = document.getElementById(stepId);
    const targetBtn = document.querySelector(`.tool-step-btn[data-studio-step="${stepId}"]`);

    if (targetStep) targetStep.style.display = 'block';
    if (targetBtn) targetBtn.classList.add('active');

    if (stepId === 'step-space' || stepId === 'step-fill') {
      renderTableGrid();
    } else if (stepId === 'step-analyze') {
      runAnalysis();
    } else if (stepId === 'step-export') {
      generateExport();
    }
  }

  function cartesianProduct(valueSets) {
    return valueSets.reduce(
      (combinations, values) =>
        combinations.flatMap(combo =>
          values.map(value => [...combo, value])
        ),
      [[]]
    );
  }

  function generateRuleSpace() {
    const valueSets = currentTable.conditions.map(c => c.values);
    const combos = cartesianProduct(valueSets);

    currentTable.rules = combos.map((combo, idx) => {
      // Preserve existing outcomes if already filled
      const existing = currentTable.rules[idx];
      return {
        id: `R-${idx + 1}`,
        combo: combo,
        outcomes: existing ? existing.outcomes : currentTable.actions.map(() => 'unresolved')
      };
    });

    const sizeEl = document.getElementById('rule-space-size');
    if (sizeEl) sizeEl.textContent = `${currentTable.rules.length} Combinations`;

    renderTableGrid();
  }

  function renderConditions() {
    const container = document.getElementById('conditions-list');
    if (!container) return;
    container.innerHTML = currentTable.conditions.map((c, i) => `
      <div style="background: rgba(15,23,42,0.8); border: 1px solid var(--border-color); padding: 12px; border-radius: 6px; margin-bottom: 10px;">
        <strong>${c.name}:</strong> <span style="color: var(--text-muted);">${c.values.join(', ')}</span>
      </div>
    `).join('');
  }

  function renderActions() {
    const container = document.getElementById('actions-list');
    if (!container) return;
    container.innerHTML = currentTable.actions.map((a, i) => `
      <div style="background: rgba(15,23,42,0.8); border: 1px solid var(--border-color); padding: 10px; border-radius: 6px; margin-bottom: 8px;">
        <span>⚡ ${a.name}</span>
      </div>
    `).join('');
  }

  function renderTableGrid() {
    const gridContainer = document.getElementById('table-grid-container');
    if (!gridContainer) return;

    if (!currentTable.rules || currentTable.rules.length === 0) {
      gridContainer.innerHTML = '<p>No rule space generated yet.</p>';
      return;
    }

    let html = `<table class="decision-table-grid"><thead><tr>
      <th style="width: 50px;">Rule</th>`;

    currentTable.conditions.forEach(c => {
      html += `<th>${c.name}</th>`;
    });
    currentTable.actions.forEach(a => {
      html += `<th style="color: #f59e0b;">${a.name}</th>`;
    });
    html += `</tr></thead><tbody>`;

    currentTable.rules.forEach((r, rIdx) => {
      html += `<tr><td><strong>${r.id}</strong></td>`;
      r.combo.forEach(val => {
        html += `<td style="color: var(--text-muted);">${val}</td>`;
      });
      r.outcomes.forEach((out, aIdx) => {
        const cellClass = `cell-${out.toLowerCase().replace(/[^a-z]/g, '')}`;
        html += `<td class="${cellClass}" onclick="DecisionEngine.cycleOutcome(${rIdx}, ${aIdx})">${out}</td>`;
      });
      html += `</tr>`;
    });

    html += `</tbody></table>`;
    gridContainer.innerHTML = html;
  }

  function cycleOutcome(rIdx, aIdx) {
    const states = ['unresolved', 'Yes', 'No', 'N/A', 'Impossible'];
    const current = currentTable.rules[rIdx].outcomes[aIdx];
    let nextIdx = (states.indexOf(current) + 1) % states.length;
    currentTable.rules[rIdx].outcomes[aIdx] = states[nextIdx];
    renderTableGrid();
  }

  function runAnalysis() {
    const total = currentTable.rules.length;
    const unresolved = currentTable.rules.filter(r => r.outcomes.includes('unresolved')).length;
    const resolved = total - unresolved;
    const pct = Math.round((resolved / total) * 100);

    const covEl = document.getElementById('analysis-coverage-meter');
    if (covEl) covEl.textContent = `${resolved} / ${total} Combinations Resolved (${pct}%)`;

    const summaryEl = document.getElementById('analysis-summary-list');
    if (!summaryEl) return;

    summaryEl.innerHTML = `
      <div class="glass-card" style="padding: 14px; margin-bottom: 10px;">
        <strong style="color: ${unresolved > 0 ? '#f43f5e' : '#34d399'};">Unresolved Rules: ${unresolved}</strong>
        <p style="font-size: 0.85rem; color: var(--text-muted);">${unresolved > 0 ? 'Some combinations do not have defined expected actions yet.' : 'All combinations resolved!'}</p>
      </div>
      <div class="glass-card" style="padding: 14px;">
        <strong style="color: #06b6d4;">Rule Optimization:</strong>
        <p style="font-size: 0.85rem; color: var(--text-muted);">Cartesian product includes all ${total} combinations. Export Gherkin scenarios for test coverage.</p>
      </div>
    `;
  }

  function generateExport() {
    const previewEl = document.getElementById('export-gherkin-preview');
    if (!previewEl) return;

    let gherkin = `# Gherkin Acceptance Scenarios for ${currentTable.title}\n\n`;

    currentTable.rules.forEach(r => {
      if (r.outcomes.includes('Yes')) {
        gherkin += `Scenario: ${r.id} - ${r.combo.join(' / ')}\n`;
        r.combo.forEach((val, i) => {
          const prefix = i === 0 ? 'Given' : 'And';
          gherkin += `  ${prefix} ${currentTable.conditions[i].name} is "${val}"\n`;
        });
        gherkin += `  When the request is evaluated\n`;
        r.outcomes.forEach((out, aIdx) => {
          if (out === 'Yes') {
            gherkin += `  Then ${currentTable.actions[aIdx].name} shall be triggered\n`;
          }
        });
        gherkin += `\n`;
      }
    });

    previewEl.textContent = gherkin || '# Fill in outcomes in Step 4 to generate Gherkin scenarios.';
  }

  function saveToProject() {
    const proj = ProjectEngine.getActiveProject();
    proj.decisionTables = proj.decisionTables || [];
    proj.decisionTables.push(currentTable);
    ProjectEngine.saveActiveProject(proj);
    alert(`Saved Decision Table "${currentTable.title}" to project "${proj.project.name}"!`);
  }

  window.DecisionEngine = {
    cycleOutcome,
    saveToProject
  };

})(window);
