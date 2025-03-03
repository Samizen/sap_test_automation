run_all: libs_install playwright_install

libs_install:
	pip -r install chatgpt_change_steps_sent/requirements.txt

playwright_install:
	playwright install