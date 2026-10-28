#!/usr/bin/env python3
"""Render the repo cards shown in this README.

Replaces readme-tools/github-readme-stats-action, which started writing
"Something went wrong" cards in July 2026 without failing the job.
Stdlib only. Exits non-zero on any API error so a broken card is never committed.

Usage: GITHUB_TOKEN=... python3 .github/scripts/render_pin_cards.py
"""
import json
import os
import sys
import textwrap
import urllib.request
from html import escape
from pathlib import Path

ORG = "AISquare-Studio"
OUT_DIR = Path(__file__).resolve().parents[2] / "profile"

# repo name -> card file under profile/. Only PUBLIC repos belong here.
CARDS = {
    "awesome-aisquare": "pin-awesome-aisquare.svg",
    "AISquare-Studio-QA": "pin-aisquare-studio-qa.svg",
    "aisquare-cli": "pin-aisquare-cli.svg",
    "pipe": "pin-pipe.svg",
}

LANG_COLORS = {
    "Python": "#3572A5",
    "TypeScript": "#3178c6",
    "JavaScript": "#f1e05a",
    "HTML": "#e34c26",
    "CSS": "#663399",
    "Shell": "#89e051",
}

REPO_ICON = "M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"
STAR_ICON = "M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z"
FORK_ICON = "M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75 0 000 1.5z"


def fetch_repo(name):
    req = urllib.request.Request(f"https://api.github.com/repos/{ORG}/{name}")
    req.add_header("Accept", "application/vnd.github+json")
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        repo = json.load(resp)
    if repo.get("private"):
        raise SystemExit(f"{ORG}/{name} is private; it cannot be shown on the public profile")
    return repo


def description_lines(text):
    lines = textwrap.wrap(text or "No description provided.", width=52)
    if len(lines) > 3:
        lines = lines[:3]
        lines[-1] = lines[-1][:49].rstrip() + "..."
    return lines


def render(repo):
    title = escape(repo["full_name"])
    lines = description_lines(repo.get("description"))
    tspans = "".join(f'<tspan dy="1.2em" x="25">{escape(line)}</tspan>' for line in lines)
    height = 120 + 16 * (len(lines) - 1)
    stats_y = 55 + 16 * len(lines) + 30

    stats, x = [], 30
    lang = repo.get("language")
    if lang:
        color = LANG_COLORS.get(lang, "#858585")
        stats.append(
            f'<g transform="translate({x}, {stats_y})"><circle cx="6" cy="-4" r="6" fill="{color}"/>'
            f'<text x="16" class="gray">{escape(lang)}</text></g>'
        )
        x += 22 + 7 * len(lang) + 20
    for icon, value in ((STAR_ICON, repo["stargazers_count"]), (FORK_ICON, repo["forks_count"])):
        stats.append(
            f'<g transform="translate({x}, {stats_y})"><svg class="icon" y="-12" viewBox="0 0 16 16" width="16" height="16">'
            f'<path fill-rule="evenodd" d="{icon}"/></svg><text x="20" class="gray">{value}</text></g>'
        )
        x += 70

    return f"""<svg width="400" height="{height}" viewBox="0 0 400 {height}" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="titleId">
  <title id="titleId">{title}</title>
  <style>
    .header {{ font: 600 18px 'Segoe UI', Ubuntu, Sans-Serif; fill: #f0883e; }}
    .description {{ font: 400 13px 'Segoe UI', Ubuntu, Sans-Serif; fill: #9f9f9f; }}
    .gray {{ font: 400 12px 'Segoe UI', Ubuntu, Sans-Serif; fill: #9f9f9f; }}
    .icon {{ fill: #79ff97; }}
  </style>
  <rect x="0.5" y="0.5" rx="4.5" width="399" height="{height - 1}" fill="#151515" stroke="#e4e2e2"/>
  <g transform="translate(25, 35)">
    <svg class="icon" x="0" y="-13" viewBox="0 0 16 16" width="16" height="16"><path fill-rule="evenodd" d="{REPO_ICON}"/></svg>
    <text x="25" y="0" class="header">{title}</text>
  </g>
  <text class="description" x="25" y="50">{tspans}</text>
  {"".join(stats)}
</svg>
"""


def main():
    for name, filename in CARDS.items():
        repo = fetch_repo(name)
        (OUT_DIR / filename).write_text(render(repo))
        print(f"wrote profile/{filename}")


if __name__ == "__main__":
    sys.exit(main())
