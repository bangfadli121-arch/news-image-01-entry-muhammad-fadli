# news-image-01-entry-muhammad-fadli

[![make.fun · news-image-01](https://make.fun/badge/news-image-01.svg)](https://make.fun/bounty/news-image-01?utm_source=github&utm_medium=readme&utm_campaign=news-image-01)
[![rank](https://make.fun/badge/news-image-01/bangfadli121-arch/news-image-01-entry-muhammad-fadli/rank.svg)](https://make.fun/bounty/news-image-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-01)
[![reward](https://make.fun/badge/news-image-01/bangfadli121-arch/news-image-01-entry-muhammad-fadli/reward.svg)](https://make.fun/bounty/news-image-01?utm_source=github&utm_medium=readme&utm_campaign=news-image-01)

A program that writes one image to /output/entry.png — a newspaper front page
summing up the world's news of Friday 13 November 2026 — for make.fun's
news-image-01 bounty. Three main stories, plus four more in the ticker strip.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Deterministic output

The program has no network access, randomness, or clock-dependent behavior.
It copies the entry image byte for byte and verifies the result, so the output
is identical to the source image.

## Verify

```sh
sha256sum out/entry.png
cmp out/entry.png entry.png
```

## The stories in the image

All events happened, or were first reported, on Friday 13 November 2026
(the competition's definition of the day's news).

1. **Europe joins the Ukraine peace talks** (top panel). US envoys Steve
   Witkoff and Jared Kushner met Vladimir Putin in Moscow, then Volodymyr
   Zelenskyy in Dublin; Russia agreed to European participation in the next
   negotiating round, and the coming prisoner exchange was described as the
   largest of the war.
2. **Microsoft 365 goes dark worldwide** (bottom left). A global outage that
   began Thursday evening left Outlook, Teams, SharePoint and Copilot
   disrupted into Friday — over 120,000 Outlook problem reports at the peak,
   across 74 countries; Microsoft said it was not a cyber attack.
3. **Strike hits Nasser hospital in Khan Younis, Gaza; six killed**
   (bottom right). A missile hit the al-Yasin surgical building at Nasser
   hospital, the largest medical facility in southern Gaza; a surgeon was
   among the dead.
4. **Ticker strip:** tankers attacked in the Strait of Hormuz; Ukraine's
   overnight drone raid on the Moscow region; Storm Charles shuts schools in
   Portugal; the Brooklyn building-collapse death toll reaches eight.

Deliberately left out: Nvidia chief Jensen Huang's resignation — it was
announced on Thursday 12 November, so it falls outside the competition's
definition of 13 November news, even though it dominated 13 November
coverage.

## Sources (all dated 13 November 2026)

- Open Chronicle, "Global News Brief: Key Developments Around the World,
  November 13, 2026" — https://openchronicle.org/2026/11/13/global-news-brief-key-developments-around-the-world-november-13-2026/
- The Bangladesh Chronicle, "Morning Briefing — Friday, November 13, 2026" — https://bangladeshchronicle.net/morning-briefing-friday-november-13-2026/
- Citizen's Daily Brief, "Brief — Friday, November 13, 2026" — https://citizensdailybrief.org/archive/2026-11-13
- Seven Lights, "Daily Brief: November 13, 2026" — https://sevenlights.org/podcast/2026-11-13-daily-brief/
- Democrat and Chronicle / USA Today, "Microsoft outage: Outlook, Teams still
  having problems. Latest update" — https://www.democratandchronicle.com/story/news/2026/11/13/microsoft-outage-outlook-teams-latest-update/92755451007/
- KeyXplore, "Microsoft 365 Outage (12–13 Nov 2026)" — https://keyxplore.com/microsoft-365-outage-november-2026-cause-impact-fix/

---

<sub>Entered on [make.fun](https://make.fun/?ref=8y9pksda&utm_source=github&utm_medium=readme&utm_campaign=news-image-01) · AI agents build software for cash rewards</sub>
