(function () {
  "use strict";
  var root = document.documentElement;

  // Theme toggle (remembered in the browser)
  document.querySelectorAll("[data-theme-toggle]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var next = root.dataset.theme === "dark" ? "light" : "dark";
      root.dataset.theme = next;
      try { localStorage.setItem("ves-theme", next); } catch (e) {}
    });
  });

  // Toast messages auto-dismiss
  function dismiss(t) { t.classList.add("hide"); setTimeout(function () { t.remove(); }, 300); }
  document.querySelectorAll(".toast").forEach(function (t, i) {
    setTimeout(function () { dismiss(t); }, 7000 + i * 600);
    var x = t.querySelector(".toast-x");
    if (x) x.addEventListener("click", function () { dismiss(t); });
  });

  // Live "inside for ..." timers and the date/time pill
  function fmt(ms) {
    var m = Math.floor(ms / 60000);
    if (m < 1) return "just now";
    var h = Math.floor(m / 60);
    return h ? h + "h " + ("0" + (m % 60)).slice(-2) + "m" : m + " min";
  }
  function tick() {
    document.querySelectorAll("[data-since]").forEach(function (el) {
      var t = Date.parse(el.dataset.since);
      if (!isNaN(t)) el.textContent = fmt(Date.now() - t);
    });
    document.querySelectorAll("[data-clock]").forEach(function (el) {
      el.textContent = new Date().toLocaleString([], { weekday: "short", day: "numeric", month: "short", hour: "2-digit", minute: "2-digit" });
    });
  }
  tick(); setInterval(tick, 20000);

  // Phone inputs accept digits only
  document.querySelectorAll("input[data-digits]").forEach(function (input) {
    input.addEventListener("input", function () { input.value = input.value.replace(/\D/g, "").slice(0, 10); });
  });

  // Stop double submits (important: every submit sends a real notification)
  document.querySelectorAll("form[data-once]").forEach(function (form) {
    form.addEventListener("submit", function () {
      var btn = form.querySelector("button[type=submit]");
      if (btn) { btn.dataset.label = btn.innerHTML; btn.disabled = true; btn.textContent = "Sending…"; }
    });
  });
  window.addEventListener("pageshow", function (e) {
    if (!e.persisted) return;
    document.querySelectorAll("form[data-once] button[type=submit]").forEach(function (btn) {
      if (btn.dataset.label) { btn.innerHTML = btn.dataset.label; btn.disabled = false; }
    });
  });

  // History search + filters
  var table = document.getElementById("hist-table");
  if (table) {
    var q = document.getElementById("hist-search"), st = document.getElementById("hist-status"),
        fl = document.getElementById("hist-flat"), empty = document.getElementById("hist-empty");
    var rows = Array.prototype.slice.call(table.tBodies[0].rows);
    var apply = function () {
      var text = q.value.trim().toLowerCase(), shown = 0;
      rows.forEach(function (r) {
        var ok = (!text || r.dataset.text.indexOf(text) > -1) && (!st.value || r.dataset.status === st.value) && (!fl.value || r.dataset.flat === fl.value);
        r.hidden = !ok; if (ok) shown++;
      });
      empty.hidden = shown > 0; table.parentNode.hidden = shown === 0;
    };
    [q, st, fl].forEach(function (el) { el.addEventListener("input", apply); el.addEventListener("change", apply); });
  }

  // Copy buttons (Telegram invite links)
  document.querySelectorAll("[data-copy]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var text = btn.dataset.copy, original = btn.innerHTML;
      var done = function () { btn.textContent = "Copied!"; setTimeout(function () { btn.innerHTML = original; }, 1500); };
      if (navigator.clipboard && window.isSecureContext !== false) {
        navigator.clipboard.writeText(text).then(done, function () { window.prompt("Copy this link:", text); });
      } else { window.prompt("Copy this link:", text); }
    });
  });

  // Edit-flat dialog
  var dlg = document.getElementById("edit-dialog");
  if (dlg) {
    document.querySelectorAll("[data-edit-flat]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        document.getElementById("edit-form").action = "/flats/" + encodeURIComponent(btn.dataset.number) + "/edit";
        document.getElementById("edit-title").textContent = btn.dataset.number;
        document.getElementById("edit-owner").value = btn.dataset.owner;
        document.getElementById("edit-phone").value = btn.dataset.phone;
        dlg.showModal();
      });
    });
    dlg.querySelector("[data-close-dialog]").addEventListener("click", function () { dlg.close(); });
    dlg.addEventListener("click", function (e) { if (e.target === dlg) dlg.close(); });
  }
})();
