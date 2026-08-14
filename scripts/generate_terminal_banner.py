import gifos

RED = "\x1b[31m"
GREEN = "\x1b[32m"
YELLOW = "\x1b[33m"
BLUE = "\x1b[34m"
MAGENTA = "\x1b[35m"
CYAN = "\x1b[36m"
RESET = "\x1b[0m"
BOLD_CYAN = "\x1b[1;36m"

t = gifos.Terminal(width=760, height=380, xpad=14, ypad=12, font_size=15)
t.set_prompt(f"{RED}gor3a{RESET}@{YELLOW}github ~> {RESET}")

t.gen_typing_text(f"{GREEN}guest@gor3a{RESET}:~$ whoami", row_num=1, speed=1)
t.gen_typing_text("mina-sameh", row_num=2, speed=1)
t.gen_text("", row_num=3)

t.gen_typing_text(f"{GREEN}guest@gor3a{RESET}:~$ neofetch", row_num=4, speed=1)

info_lines = [
    f"{BOLD_CYAN}Mina Sameh{RESET}",
    f"{CYAN}------------------{RESET}",
    f"{YELLOW}Role{RESET}      Senior Software Engineer",
    f"{YELLOW}Stack{RESET}     TypeScript, React/Next.js, Node/NestJS, React Native",
    f"{YELLOW}DB{RESET}        PostgreSQL, MongoDB, Redis",
    f"{YELLOW}Infra{RESET}     Docker, AWS, GraphQL",
    f"{YELLOW}Site{RESET}      minasameh.com",
    f"{YELLOW}Status{RESET}    {MAGENTA}open to work{RESET}",
]
t.gen_text(info_lines, row_num=5, prompt=True)

t.gen_gif()
