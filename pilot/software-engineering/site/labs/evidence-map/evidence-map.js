/* Evidence Map — Graph Engine & BFS Impact Analyzer */

(function(window) {
  'use strict';

  let cyInstance = null;
  let graphData = { nodes: [], edges: [] };
  let selectedNodeId = null;

  const NODE_COLORS = {
    goal: '#38bdf8',
    need: '#818cf8',
    requirement: '#a78bfa',
    assumption: '#f59e0b',
    decision: '#fb923c',
    component: '#34d399',
    test: '#4ade80',
    metric: '#e879f9',
    incident: '#f87171'
  };

  document.addEventListener('DOMContentLoaded', () => {
    loadGraphData();
    initMapEvents();
  });

  function loadGraphData() {
    fetch('content/flagship-case.json')
      .then(r => r.json())
      .then(data => {
        graphData = data;
        initCytoscape(data);
      })
      .catch(err => {
        console.warn('Could not load flagship case JSON:', err);
        // Fallback starter graph if fetch fails
        const starter = ProjectEngine.getActiveProject();
        graphData = {
          nodes: starter.traceNodes || [],
          edges: starter.traceEdges || []
        };
        initCytoscape(graphData);
      });
  }

  function initCytoscape(data) {
    if (typeof cytoscape === 'undefined') {
      console.warn('Cytoscape JS not loaded yet');
      return;
    }

    const elements = [];

    (data.nodes || []).forEach(n => {
      elements.push({
        data: {
          id: n.id,
          label: `${n.id}: ${n.title}`,
          type: n.type,
          color: NODE_COLORS[n.type] || '#38bdf8'
        }
      });
    });

    (data.edges || []).forEach(e => {
      elements.push({
        data: {
          id: `${e.source}->${e.target}`,
          source: e.source,
          target: e.target,
          label: e.type || 'relates'
        }
      });
    });

    cyInstance = cytoscape({
      container: document.getElementById('cy-canvas'),
      elements: elements,
      style: [
        {
          selector: 'node',
          style: {
            'background-color': 'data(color)',
            'label': 'data(label)',
            'color': '#e2e8f0',
            'font-size': '11px',
            'text-valign': 'bottom',
            'text-margin-y': '6px',
            'width': '36px',
            'height': '36px',
            'border-width': '2px',
            'border-color': 'rgba(255,255,255,0.2)'
          }
        },
        {
          selector: 'edge',
          style: {
            'width': 2,
            'line-color': 'rgba(255,255,255,0.2)',
            'target-arrow-color': 'rgba(255,255,255,0.3)',
            'target-arrow-shape': 'triangle',
            'curve-style': 'bezier',
            'label': 'data(label)',
            'font-size': '9px',
            'color': '#64748b',
            'text-rotation': 'autorotate'
          }
        },
        {
          selector: '.highlight-impact',
          style: {
            'background-color': '#f43f5e',
            'line-color': '#f43f5e',
            'target-arrow-color': '#f43f5e',
            'border-color': '#fff',
            'border-width': '3px'
          }
        },
        {
          selector: '.highlight-upstream',
          style: {
            'background-color': '#38bdf8',
            'border-color': '#fff',
            'border-width': '3px'
          }
        }
      ],
      layout: {
        name: 'breadthfirst',
        directed: true,
        padding: 20,
        spacingFactor: 1.25
      }
    });

    cyInstance.on('tap', 'node', function(evt) {
      const node = evt.target;
      selectedNodeId = node.id();
      renderNodeDetails(node.id());
    });
  }

  function initMapEvents() {
    const btnSim = document.getElementById('btn-simulate-impact');
    if (btnSim) {
      btnSim.addEventListener('click', runImpactSimulation);
    }

    const btnOrphans = document.getElementById('btn-check-orphans');
    if (btnOrphans) {
      btnOrphans.addEventListener('click', checkOrphans);
    }
  }

  function renderNodeDetails(nodeId) {
    const nodeObj = graphData.nodes.find(n => n.id === nodeId);
    const container = document.getElementById('node-detail-panel');
    if (!container || !nodeObj) return;

    container.innerHTML = `
      <div class="glass-card" style="padding: 16px; border-left: 4px solid ${NODE_COLORS[nodeObj.type] || '#38bdf8'};">
        <span style="font-size: 0.75rem; font-weight: 700; color: ${NODE_COLORS[nodeObj.type] || '#38bdf8'}; text-transform: uppercase;">${nodeObj.type}</span>
        <h4 style="font-size: 1.05rem; font-weight: 700; margin: 4px 0 8px 0;">${nodeObj.id}: ${nodeObj.title}</h4>
        <div style="font-size: 0.8rem; color: var(--text-dim); margin-bottom: 10px;">Status: ${nodeObj.status || 'Active'}</div>
        <button onclick="EvidenceEngine.runImpactSimulation('${nodeObj.id}')" class="tool-step-btn" style="background: #f43f5e; color: #fff; border: none; padding: 4px 10px; font-size: 0.8rem;">Simulate Change Impact</button>
      </div>
    `;
  }

  function findDownstreamNodes(startId) {
    const edges = graphData.edges;
    const visited = new Set([startId]);
    const queue = [startId];

    while (queue.length > 0) {
      const current = queue.shift();
      edges.filter(e => e.source === current).forEach(e => {
        if (!visited.has(e.target)) {
          visited.add(e.target);
          queue.push(e.target);
        }
      });
    }
    visited.delete(startId);
    return Array.from(visited);
  }

  function runImpactSimulation(targetId) {
    const id = targetId || selectedNodeId || 'R-1';
    if (!cyInstance) return;

    cyInstance.elements().removeClass('highlight-impact').removeClass('highlight-upstream');

    const downstream = findDownstreamNodes(id);
    
    // Highlight root node & downstream reachables
    cyInstance.getElementById(id).addClass('highlight-impact');
    downstream.forEach(dId => {
      cyInstance.getElementById(dId).addClass('highlight-impact');
    });

    const reportEl = document.getElementById('impact-report-output');
    if (reportEl) {
      reportEl.innerHTML = `
        <div class="glass-card" style="padding: 16px; border: 1px solid #f43f5e; background: rgba(244,63,94,0.08);">
          <strong style="color: #fb7185;">Change Footprint Report for ${id}</strong>
          <p style="font-size: 0.85rem; margin-top: 6px; color: var(--text-main);">
            Modifying <strong>${id}</strong> potentially impacts ${downstream.length} downstream artifacts:
          </p>
          <ul style="margin-left: 20px; font-size: 0.85rem; margin-top: 6px; color: var(--text-muted);">
            ${downstream.map(d => `<li><strong>${d}</strong> (${graphData.nodes.find(n => n.id === d)?.type || 'node'})</li>`).join('')}
          </ul>
        </div>
      `;
    }
  }

  function checkOrphans() {
    if (!cyInstance) return;
    const connected = new Set();
    graphData.edges.forEach(e => { connected.add(e.source); connected.add(e.target); });
    const orphans = graphData.nodes.filter(n => !connected.has(n.id));

    alert(orphans.length > 0 ? `Found ${orphans.length} orphaned nodes: ${orphans.map(o=>o.id).join(', ')}` : 'No orphaned nodes found! All artifacts are connected.');
  }

  function saveToProject() {
    const proj = ProjectEngine.getActiveProject();
    proj.traceNodes = graphData.nodes;
    proj.traceEdges = graphData.edges;
    ProjectEngine.saveActiveProject(proj);
    alert(`Saved Evidence Map graph (${graphData.nodes.length} nodes) to project "${proj.project.name}"!`);
  }

  window.EvidenceEngine = {
    runImpactSimulation,
    saveToProject
  };

})(window);
