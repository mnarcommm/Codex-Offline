import os
import subprocess
import time

GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"


def clear_screen():
    os.system("clear")


def print_banner():
    clear_screen()
    print(f"{CYAN}========================================================={RESET}")
    print(f"{GREEN}   CODEX - Offline CyberSec & Public Web Builder (No AI) {RESET}")
    print(f"{CYAN}========================================================={RESET}")
    print(f"{YELLOW}[*] Mode: English Prompts | Local Templates | Public Link{RESET}\n")


def start_public_server(folder_path, port=8000):
    print(f"\n{CYAN}[*] Starting local server on port {port}...{RESET}")
    server_process = subprocess.Popen(
        ["python", "-m", "http.server", str(port)],
        cwd=folder_path,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(2)

    print(f"{YELLOW}[*] Generating public link for everyone using SSH tunnel...{RESET}")
    print(f"{GREEN}[!] Share the generated '.lhr.life' link with anyone! Press Ctrl+C to stop.{RESET}\n")

    try:
        subprocess.run(
            ["ssh", "-o", "StrictHostKeyChecking=no", "-R", f"80:localhost:{port}", "nokey@localhost.run"]
        )
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Stopping server...{RESET}")
    finally:
        server_process.terminate()


def get_games_website_html():
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>CODEX Arcade - Games Hub</title>
  <style>
    * { box-sizing: border-box; font-family: Arial, sans-serif; }
    body { margin: 0; background: #0d1117; color: #e6edf3; text-align: center; }
    header { padding: 24px; background: #161b22; border-bottom: 1px solid #30363d; }
    h1 { margin: 0; color: #58a6ff; }
    .container { max-width: 900px; margin: 30px auto; padding: 0 16px; }
    .game-box { background: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 20px; margin-bottom: 24px; }
    canvas { background: #010409; border: 2px solid #58a6ff; border-radius: 8px; display: block; margin: 15px auto; max-width: 100%; }
    button { background: #238636; color: #fff; border: none; padding: 10px 18px; border-radius: 6px; cursor: pointer; font-size: 15px; margin: 5px; }
    button:hover { background: #2ea043; }
    input { padding: 10px; border-radius: 6px; border: 1px solid #30363d; background: #0d1117; color: #fff; width: 140px; text-align: center; }
    .status { margin-top: 10px; font-weight: bold; color: #79c0ff; }
  </style>
</head>
<body>
  <header>
    <h1>CODEX Games Website</h1>
    <p>Play instant browser games & share this link with anyone.</p>
  </header>

  <div class="container">
    <div class="game-box">
      <h2>1. Dodge The Blocks</h2>
      <p>Use Left / Right arrows or tap buttons below.</p>
      <canvas id="gameCanvas" width="360" height="420"></canvas>
      <div>
        <button onclick="moveLeft()">Left</button>
        <button onclick="moveRight()">Right</button>
        <button onclick="resetGame()">Restart</button>
      </div>
      <div class="status" id="scoreText">Score: 0</div>
    </div>

    <div class="game-box">
      <h2>2. Guess The Number (1 - 100)</h2>
      <input type="number" id="guessInput" min="1" max="100" placeholder="1 - 100" />
      <button onclick="checkGuess()">Guess</button>
      <div class="status" id="guessResult">Enter a number to start!</div>
    </div>
  </div>

  <script>
    const canvas = document.getElementById("gameCanvas");
    const ctx = canvas.getContext("2d");
    let playerX = 160, score = 0, gameOver = false;
    let enemy = { x: Math.floor(Math.random() * 320), y: 0, w: 40, h: 25, speed: 4 };

    function moveLeft() { if (!gameOver) playerX = Math.max(0, playerX - 30); }
    function moveRight() { if (!gameOver) playerX = Math.min(canvas.width - 40, playerX + 30); }
    function resetGame() { playerX = 160; score = 0; gameOver = false; enemy.y = 0; enemy.speed = 4; document.getElementById("scoreText").innerText = "Score: 0"; }

    document.addEventListener("keydown", (e) => {
      if (e.key === "ArrowLeft") moveLeft();
      if (e.key === "ArrowRight") moveRight();
    });

    function loop() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      if (!gameOver) {
        enemy.y += enemy.speed;
        if (enemy.y > canvas.height) {
          enemy.y = -25;
          enemy.x = Math.floor(Math.random() * (canvas.width - 40));
          score++;
          enemy.speed = Math.min(10, 4 + score * 0.25);
          document.getElementById("scoreText").innerText = "Score: " + score;
        }
        if (enemy.y + enemy.h >= canvas.height - 35 && enemy.x < playerX + 40 && enemy.x + enemy.w > playerX) {
          gameOver = true;
          document.getElementById("scoreText").innerText = "Game Over! Final Score: " + score;
        }
      }
      ctx.fillStyle = "#58a6ff";
      ctx.fillRect(playerX, canvas.height - 35, 40, 20);
      ctx.fillStyle = "#f85149";
      ctx.fillRect(enemy.x, enemy.y, enemy.w, enemy.h);
      requestAnimationFrame(loop);
    }
    loop();

    let secret = Math.floor(Math.random() * 100) + 1;
    function checkGuess() {
      const val = parseInt(document.getElementById("guessInput").value);
      const res = document.getElementById("guessResult");
      if (!val) { res.innerText = "Please enter a valid number."; return; }
      if (val === secret) {
        res.innerText = "Correct! New secret number generated.";
        secret = Math.floor(Math.random() * 100) + 1;
      } else if (val < secret) {
        res.innerText = "Too low! Try higher.";
      } else {
        res.innerText = "Too high! Try lower.";
      }
    }
  </script>
</body>
</html>
"""


def get_cyber_tool_script(prompt_lower):
    if "port" in prompt_lower or "scan" in prompt_lower:
        return """import socket

target = input("Enter target IP or domain: ").strip()
ports_input = input("Enter ports (e.g. 21,22,80,443) or press Enter for common ports: ").strip()

if ports_input:
    ports = [int(p.strip()) for p in ports_input.split(",") if p.strip().isdigit()]
else:
    ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 8080]

print(f"\\n[*] Scanning {target}...")
for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} is OPEN")
    else:
        print(f"[-] Port {port} is closed")
    s.close()
"""
    else:
        return """import hashlib
import random
import string

print("=== CODEX CyberSec Utility (Password & Hash Generator) ===")
length = int(input("Password length (default 16): ") or "16")
chars = string.ascii_letters + string.digits + "!@#$%^&*"
password = "".join(random.choice(chars) for _ in range(length))

md5_hash = hashlib.md5(password.encode()).hexdigest()
sha256_hash = hashlib.sha256(password.encode()).hexdigest()

print(f"\\n[+] Generated Password : {password}")
print(f"[+] MD5 Hash           : {md5_hash}")
print(f"[+] SHA256 Hash        : {sha256_hash}")
"""


def build_website(html_content):
    project_dir = "codex_web_project"
    os.makedirs(project_dir, exist_ok=True)
    file_path = os.path.join(project_dir, "index.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"{GREEN}[+] Website created at: {file_path}{RESET}")
    deploy = input(f"{YELLOW}[?] Publish online for everyone now? (y/n): {RESET}").strip().lower()
    if deploy == "y":
        start_public_server(project_dir, 8000)


def build_and_run_tool(py_code):
    tool_path = "cyber_tool.py"
    with open(tool_path, "w", encoding="utf-8") as f:
        f.write(py_code)
    print(f"{GREEN}[+] Cybersecurity tool created at: {tool_path}{RESET}")
    run_now = input(f"{YELLOW}[?] Run {tool_path} now? (y/n): {RESET}").strip().lower()
    if run_now == "y":
        subprocess.run(["python", tool_path])


def main():
    print_banner()
    while True:
        prompt = input(f"{GREEN}codex@cybersec ~ $ {RESET}").strip()
        if not prompt:
            continue
        low = prompt.lower()

        if low in ["exit", "quit"]:
            print(f"{RED}[!] Exiting CODEX...{RESET}")
            break

        if low.startswith("http://") or low.startswith("https://"):
            print(f"{CYAN}[*] Cloning repository: {prompt}{RESET}")
            subprocess.run(["git", "clone", prompt])
            continue

        if "website" in low or "game" in low or "web" in low:
            build_website(get_games_website_html())
        elif "tool" in low or "scan" in low or "port" in low or "password" in low or "hash" in low or "cyber" in low:
            build_and_run_tool(get_cyber_tool_script(low))
        else:
            print(f"{YELLOW}[!] Try English prompts like:{RESET}")
            print("  - Create a website for me, a website with games.")
            print("  - Create a port scanner tool")
            print("  - Create a password and hash tool")
            print("  - https://github.com/user/repo.git")


if __name__ == "__main__":
    main()

