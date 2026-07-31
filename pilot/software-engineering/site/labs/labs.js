/* Requirements Workbench — Shared Project Storage & Navigation Engine */

(function(window) {
  'use strict';

  const STORAGE_KEY = 'bbt_lab_projects';
  const ACTIVE_PROJECT_KEY = 'bbt_lab_active_project_id';

  // Default Pathways Flagship Starter Project
  const PATHWAYS_STARTER_PROJECT = {
    project: {
      id: "proj-pathways",
      name: "Community Programs Hub (Pathways)",
      description: "Nonprofit coordination platform managing school sessions, volunteer attendance, reporting periods, and post-completion audit logs.",
      created: "2026-07-31T00:00:00Z",
      modified: "2026-07-31T00:00:00Z",
      isStarter: true
    },
    requirements: [
      {
        id: "REQ-ATT-001",
        title: "Amend completed-session attendance",
        statement: "When an authorized program administrator discovers an attendance error, the session-management system shall permit the administrator to amend student or volunteer attendance while the reporting period remains open.",
        type: "functional",
        source: "Director of Programs",
        rationale: "Attendance corrections are required for accurate participation metrics and partner reporting.",
        priority: "high",
        maturity: "accepted-obligation",
        open_questions: ["Who can reopen a locked reporting period?"],
        acceptance_criteria: [
          "Given a completed session in an open reporting period and user is Program Administrator, when attendance is changed, then the change is saved with audit trail."
        ],
        swebok_links: ["3.1", "9.3"],
        revisions: []
      }
    ],
    decisionTables: [
      {
        id: "DT-ATT-001",
        title: "Attendance Editing Permissions",
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
        rules: [],
        linked_requirements: ["REQ-ATT-001"]
      }
    ],
    traceNodes: [
      { id: "G-1", type: "goal", title: "Improve accuracy of participation reporting", status: "active" },
      { id: "N-1", type: "need", title: "Program staff need to correct attendance errors", status: "active" },
      { id: "REQ-ATT-001", type: "requirement", title: "Amend completed-session attendance", status: "active" },
      { id: "A-1", type: "assumption", title: "Reporting periods have clearly recorded status", status: "active" },
      { id: "D-1", type: "decision", title: "Store corrections in append-only audit table", status: "active" },
      { id: "C-1", type: "component", title: "Attendance Editor Service", status: "active" },
      { id: "T-1", type: "test", title: "Administrator edits completed session attendance", status: "active" },
      { id: "M-1", type: "metric", title: "Percentage of completed sessions with attendance", status: "active" }
    ],
    traceEdges: [
      { source: "G-1", target: "N-1", type: "derived-from", confidence: "confirmed" },
      { source: "N-1", target: "REQ-ATT-001", type: "satisfies", confidence: "confirmed" },
      { source: "REQ-ATT-001", target: "D-1", type: "implemented-by", confidence: "confirmed" },
      { source: "REQ-ATT-001", target: "T-1", type: "verified-by", confidence: "confirmed" },
      { source: "D-1", target: "C-1", type: "implemented-by", confidence: "confirmed" },
      { source: "REQ-ATT-001", target: "M-1", type: "verified-by", confidence: "confirmed" }
    ]
  };

  const ProjectEngine = {
    init: function() {
      let projects = this.getProjects();
      if (!projects || projects.length === 0) {
        projects = [PATHWAYS_STARTER_PROJECT];
        this.saveProjects(projects);
        this.setActiveProjectId("proj-pathways");
      }
    },

    getProjects: function() {
      try {
        const raw = localStorage.getItem(STORAGE_KEY);
        return raw ? JSON.parse(raw) : [];
      } catch(e) {
        console.warn('LocalStorage error:', e);
        return [PATHWAYS_STARTER_PROJECT];
      }
    },

    saveProjects: function(projects) {
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(projects));
      } catch(e) {
        console.warn('LocalStorage save error:', e);
      }
    },

    getActiveProjectId: function() {
      return localStorage.getItem(ACTIVE_PROJECT_KEY) || "proj-pathways";
    },

    setActiveProjectId: function(id) {
      localStorage.setItem(ACTIVE_PROJECT_KEY, id);
    },

    getActiveProject: function() {
      const activeId = this.getActiveProjectId();
      const projects = this.getProjects();
      return projects.find(p => p.project.id === activeId) || projects[0] || PATHWAYS_STARTER_PROJECT;
    },

    saveActiveProject: function(projData) {
      const projects = this.getProjects();
      const idx = projects.findIndex(p => p.project.id === projData.project.id);
      projData.project.modified = new Date().toISOString();
      if (idx >= 0) {
        projects[idx] = projData;
      } else {
        projects.push(projData);
      }
      this.saveProjects(projects);
    },

    createProject: function(name, description) {
      const newProj = {
        project: {
          id: 'proj-' + Date.now(),
          name: name || 'New Requirements Project',
          description: description || '',
          created: new Date().toISOString(),
          modified: new Date().toISOString(),
          isStarter: false
        },
        requirements: [],
        decisionTables: [],
        traceNodes: [],
        traceEdges: []
      };
      const projects = this.getProjects();
      projects.push(newProj);
      this.saveProjects(projects);
      this.setActiveProjectId(newProj.project.id);
      return newProj;
    },

    deleteProject: function(id) {
      let projects = this.getProjects();
      projects = projects.filter(p => p.project.id !== id);
      if (projects.length === 0) {
        projects = [PATHWAYS_STARTER_PROJECT];
      }
      this.saveProjects(projects);
      this.setActiveProjectId(projects[0].project.id);
    },

    exportProjectJSON: function(id) {
      const projects = this.getProjects();
      const proj = projects.find(p => p.project.id === id) || projects[0];
      const blob = new Blob([JSON.stringify(proj, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `${proj.project.name.toLowerCase().replace(/[^a-z0-9]/g, '-')}-workbench.json`;
      a.click();
      URL.revokeObjectURL(url);
    }
  };

  ProjectEngine.init();
  window.ProjectEngine = ProjectEngine;

})(window);
