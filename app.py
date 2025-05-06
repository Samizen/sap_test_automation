import streamlit as st
import os
import re
import subprocess

TEST_DIR = "test_playwright"

st.set_page_config(page_title="Playwright Test Runner", layout="wide")

st.title("🎭 Playwright Test Dashboard")

# --- Sidebar: List of Test Files ---
test_files = [f for f in os.listdir(TEST_DIR) if f.endswith(".py")]
test_files.sort()

selected_test = st.sidebar.radio("📂 Select a Test Case", test_files)

if selected_test:
    file_path = os.path.join(TEST_DIR, selected_test)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.readlines()

    # --- Extract parameters before first function ---
    param_lines = []
    body_lines = []
    func_started = False

    for line in content:
        if line.strip().startswith("def "):
            func_started = True
        if not func_started:
            param_lines.append(line)
        else:
            body_lines.append(line)

    param_dict = {}
    for line in param_lines:
        match = re.match(r'^(\w+)\s*=\s*(.+)', line)
        if match:
            var, val = match.groups()
            param_dict[var] = val.strip()

    st.header(f"🧪 {selected_test}")
    st.markdown("---")

    # --- Edit Parameters Form ---
    with st.form(f"form_{selected_test}"):
        st.subheader("🛠️ Edit Parameters:")
        updated_params = {}
        for k, v in param_dict.items():
            default_val = re.sub(r'^["\']|["\']$', '', v)  # strip quotes
            new_val = st.text_input(k, default_val, key=f"{selected_test}_{k}")
            updated_params[k] = f'"{new_val}"' if v.startswith(('"', "'")) else new_val

        save_button = st.form_submit_button("💾 Save Parameters")

        if save_button:
            with open(file_path, 'w', encoding='utf-8') as f:
                for k, v in updated_params.items():
                    f.write(f"{k} = {v}\n")
                f.writelines(body_lines)
            st.success("✅ Parameters updated successfully!")

    # --- Run Button ---
    if st.button("▶ Run Test"):
        with st.spinner("Running test..."):
            result = subprocess.run(
                ["pytest", file_path],
                capture_output=True,
                text=True
            )
            st.subheader("📄 Test Output:")
            st.code(result.stdout + result.stderr, language="bash")
