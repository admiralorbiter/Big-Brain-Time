/* SWEBOK v4.0 Interactive Wiki - Global JavaScript Engine */

(function() {
  'use strict';

  // State Management
  const STORAGE_KEY_PROGRESS = 'swebok_v4_progress';

  // Tooltip Dictionary for Quick Hover Concepts
  const DICTIONARY = {
    "functional requirement": "Specifies observable behaviors, policies, or processes the software must provide to solve a problem.",
    "nonfunctional requirement": "Constrains how the solution is delivered, including technology constraints and Quality of Service (QoS) constraints.",
    "technology constraint": "Mandates or prohibits the use of specific hardware, databases, frameworks, or programming languages.",
    "quality of service constraint": "Specifies acceptable performance levels (speed, security, reliability, availability) without dictating technology.",
    "derived requirement": "A requirement imposed internally by architectural or design choices rather than external business stakeholders.",
    "atdd": "Acceptance Test-Driven Development: Writing automated acceptance criteria before implementation code is produced.",
    "bdd": "Behavior-Driven Development: Formulating requirements as executable Given-When-Then user stories and scenarios.",
    "swebok": "Software Engineering Body of Knowledge published by the IEEE Computer Society.",
    "ka": "Knowledge Area: One of the 18 core software engineering disciplines in SWEBOK v4.0."
  };

  document.addEventListener('DOMContentLoaded', () => {
    initProgressTracker();
    initTooltipEngine();
    initNotesSidecars();
  });

  // Progress Tracking System
  function initProgressTracker() {
    let progress = {};
    try {
      progress = JSON.parse(localStorage.getItem(STORAGE_KEY_PROGRESS) || '{}');
    } catch(e) {
      console.warn('LocalStorage not available');
    }

    // Mark current page if topic
    const currentTopic = document.body.dataset.topicId;
    if (currentTopic) {
      progress[currentTopic] = {
        visited: true,
        lastSeen: new Date().toISOString()
      };
      try {
        localStorage.setItem(STORAGE_KEY_PROGRESS, JSON.stringify(progress));
      } catch(e){}
    }

    // Update status indicators on page links
    document.querySelectorAll('[data-topic-link]').forEach(el => {
      const topicId = el.dataset.topicLink;
      if (progress[topicId]?.visited) {
        el.classList.add('completed-topic');
      }
    });
  }

  // Hover Tooltip Engine
  function initTooltipEngine() {
    let tooltipEl = document.getElementById('global-tooltip');
    if (!tooltipEl) {
      tooltipEl = document.createElement('div');
      tooltipEl.id = 'global-tooltip';
      tooltipEl.className = 'tooltip-popup';
      document.body.appendChild(tooltipEl);
    }

    document.querySelectorAll('.concept-pill, [data-term]').forEach(el => {
      const termKey = (el.dataset.term || el.textContent).trim().toLowerCase();
      const def = DICTIONARY[termKey];
      if (!def) return;

      el.addEventListener('mouseenter', (e) => {
        tooltipEl.textContent = def;
        tooltipEl.classList.add('visible');
        positionTooltip(e, tooltipEl);
      });

      el.addEventListener('mousemove', (e) => {
        positionTooltip(e, tooltipEl);
      });

      el.addEventListener('mouseleave', () => {
        tooltipEl.classList.remove('visible');
      });
    });
  }

  function positionTooltip(e, tooltipEl) {
    const offset = 12;
    let left = e.clientX + offset;
    let top = e.clientY + offset;

    // Boundary check
    if (left + 320 > window.innerWidth) {
      left = e.clientX - 320 - offset;
    }
    if (top + 100 > window.innerHeight) {
      top = e.clientY - 100 - offset;
    }

    tooltipEl.style.left = `${left}px`;
    tooltipEl.style.top = `${top}px`;
  }

  // Notes Sidecar Loader (.notes.json)
  function initNotesSidecars() {
    const sidecarContainer = document.getElementById('sidecar-content');
    const topicId = document.body.dataset.topicId;
    if (!sidecarContainer || !topicId) return;

    fetch(`./${topicId}.notes.json`)
      .then(res => {
        if (!res.ok) throw new Error('No sidecar notes yet');
        return res.json();
      })
      .then(data => {
        renderSidecar(data, sidecarContainer);
      })
      .catch(err => {
        sidecarContainer.innerHTML = '<p style="color: var(--text-dim); font-size: 0.85rem; font-style: italic;">No additional notes or BBT links added yet for this topic.</p>';
      });
  }

  function renderSidecar(data, container) {
    let html = '';

    if (data.fieldContext && data.fieldContext.length > 0) {
      html += `<div class="layer-box field-context">
        <span class="layer-label">Field Context (2025+)</span>`;
      data.fieldContext.forEach(item => {
        html += `<p style="font-size: 0.9rem; margin-bottom: 6px;">${item.note}</p>`;
        if (item.source) html += `<span style="font-size: 0.75rem; color: var(--text-dim);">— ${item.source}</span>`;
      });
      html += `</div>`;
    }

    if (data.personalNotes && data.personalNotes.length > 0) {
      html += `<div class="layer-box personal">
        <span class="layer-label">Personal Notes & Reflection</span>`;
      data.personalNotes.forEach(note => {
        html += `<p style="font-size: 0.9rem; margin-bottom: 6px;">${note}</p>`;
      });
      html += `</div>`;
    }

    if (data.externalLinks && data.externalLinks.length > 0) {
      html += `<div style="margin-top: 16px;">
        <h4 style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; color: var(--text-dim); margin-bottom: 8px;">BBT & External Corpus Links</h4>
        <ul style="list-style: none;">`;
      data.externalLinks.forEach(link => {
        html += `<li style="margin-bottom: 6px;"><a href="${link.url}" target="_blank" style="font-size: 0.85rem;">🔗 ${link.label}</a></li>`;
      });
      html += `</ul></div>`;
    }

    container.innerHTML = html || '<p style="color: var(--text-dim); font-size: 0.85rem;">Sidecar initialized (empty).</p>';
  }

})();
