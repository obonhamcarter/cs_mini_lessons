<script>
(function () {
  const STORAGE_KEY = "cs-quest-theme";
  const DEFAULT_THEME = "professional";

  function applyTheme(theme) {
    const activeTheme = theme === "castle" ? "castle" : DEFAULT_THEME;
    document.documentElement.setAttribute("data-theme", activeTheme);
    localStorage.setItem(STORAGE_KEY, activeTheme);

    const checkbox = document.getElementById("theme-switch-checkbox");
    if (checkbox) {
      checkbox.checked = activeTheme === "castle";
      checkbox.setAttribute("aria-checked", String(checkbox.checked));
    }

    const label = document.getElementById("theme-switch-label");
    if (label) {
      label.textContent = activeTheme === "castle" ? "Castle" : "Professional";
    }

    const icon = document.querySelector("#theme-switch-wrapper .theme-switch-icon");
    if (icon) {
      icon.textContent = activeTheme === "castle" ? "🏰" : "💼";
    }
  }

  function getStoredTheme() {
    const savedTheme = localStorage.getItem(STORAGE_KEY);
    return savedTheme === "castle" ? "castle" : DEFAULT_THEME;
  }

  function createToggle() {
    const rightNav = document.querySelector("#quarto-header .navbar-nav.ms-auto");

    if (!rightNav || document.getElementById("theme-switch-wrapper")) {
      return;
    }

    const wrapper = document.createElement("li");
    wrapper.className = "nav-item";
    wrapper.id = "theme-switch-wrapper";

    const control = document.createElement("div");
    control.className = "theme-switch-control";

    const icon = document.createElement("span");
    icon.className = "theme-switch-icon";
    icon.textContent = "💼";

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.className = "form-check-input";
    checkbox.id = "theme-switch-checkbox";
    checkbox.setAttribute("role", "switch");
    checkbox.setAttribute("aria-label", "Toggle site theme between professional and castle");

    const label = document.createElement("span");
    label.id = "theme-switch-label";
    label.className = "theme-switch-label";

    checkbox.addEventListener("change", function () {
      applyTheme(this.checked ? "castle" : DEFAULT_THEME);
    });

    control.appendChild(icon);
    control.appendChild(checkbox);
    control.appendChild(label);
    wrapper.appendChild(control);

    const firstRightNavItem = rightNav.querySelector(":scope > .nav-item");
    if (firstRightNavItem) {
      rightNav.insertBefore(wrapper, firstRightNavItem);
    } else {
      rightNav.appendChild(wrapper);
    }

    applyTheme(getStoredTheme());
  }

  document.addEventListener("DOMContentLoaded", function () {
    applyTheme(getStoredTheme());
    createToggle();
  });
})();
</script>
