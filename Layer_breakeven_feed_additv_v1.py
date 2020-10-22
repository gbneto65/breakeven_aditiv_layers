# Guilherme - Jun 2019
# Breakeven - Layers - V - beta .95
# tringular density function
import os
# -------------------------------------------------------------
# ------------------ input parameters -------------------------
# -------------------------------------------------------------
# define input variables - sequence: min, max, most probably
#
period_weeks = [100]
eggs_hen_total = [380, 400, 390] # min , max & MP
feed_price = [200, 300, 250]  # $$$ - min , max & MP
egg_price_100un = [3, 10, 4]  # % values
addit_price_kg = [5]  # $$$ / kg of feed additive
inclusion_ton = [.25] # kg / ton of feed
feed_cons_day = [.1]  # 100g / day / hen
case_name = "D´Heus - Aranda"  # customer name
savefigurepath = os.path.dirname(os.path.realpath(__file__))

#savefigurepath = "/Users/Usuario/Desktop/python/" # folder path to store the chart figure (output)
savefigurefilename = "/layer_case_" # name of the file of the output
graph_dpi = 200  # resolution of chart in dpi

egg_production_improvement = [.9]  # (%) expected improvement with probiotc
breakevenprob_profit_percent = 75  # (%) - probability of the break-even from up is considered profitable area (number from 0 to 100)

n = 200000  # number of repetitions - ideal 10K or more

##################################################################
# facecolor_chart = '#E0E0E0'
facecolor_chart = 'darkgray'
background_chart_color_profit = "darkgreen"
background_chart_color_nonprofit = "tomato"
background_chart_color_alpha = .4
chart_alpha = .9

xaxis_font_size = 7
yaxis_font_size = 7

profitable_msn = "Profitable Region"

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import random as rd
import statistics as st
import os
import time
import numpy as np

todaysdate = time.strftime("%d/%m/%Y")
egg_produ_improv = egg_production_improvement[0]
egg_improv = egg_production_improvement[0]


def cls():  # clean console function
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

x_period_weeks = []
x_eggs_hen_total = []
x_feed_price = []
x_egg_price_100un = []
x_addit_price_kg = []
x_inclusion_ton = []
x_feed_cons_day = []

days_total = []
egg_price_un = []
vol_feed_hen = []
cost_feed_hen = []
vol_addit_hen = []
cost_addit_hen = []

for i in range(0, n):
    r = period_weeks[0]
    x_period_weeks.append(r)

for i in range(0, n):
    r = rd.triangular(eggs_hen_total[0],
                      eggs_hen_total[1],
                      eggs_hen_total[2])
    x_eggs_hen_total.append(round(r, 0))

for i in range(0, n):
    r = rd.triangular(feed_price[0],
                      feed_price[1],
                      feed_price[2])
    x_feed_price.append(r)

for i in range(0, n):
    r = eggs_hen_total[0]
    x_eggs_hen_total.append(r)

for i in range(0, n):
    r = addit_price_kg[0]
    x_addit_price_kg.append(r)

for i in range(0, n):
    r = inclusion_ton[0]
    x_inclusion_ton.append(r)

for i in range(0, n):
    r = rd.triangular(egg_price_100un[0],
                      egg_price_100un[1],
                      egg_price_100un[2])
    x_egg_price_100un.append(r)

for i in range(0, n):
    r = feed_cons_day[0]
    x_feed_cons_day.append(r)

# ------------------------------------------

for i in range(0, n):
    r = x_period_weeks[i] * 7
    days_total.append(r)

for i in range(0, n):
    r = x_feed_cons_day[i] * days_total[i]
    vol_feed_hen.append(r)

for i in range(0, n):
    r = vol_feed_hen[i] * x_feed_price[i] / 1000
    cost_feed_hen.append(r)

for i in range(0, n):
    r = vol_feed_hen[i] * x_inclusion_ton[i] / 1000
    vol_addit_hen.append(r)

for i in range(0, n):
    r = vol_addit_hen[i] * x_addit_price_kg[i]
    cost_addit_hen.append(r)

for i in range(0, n):
    r = x_egg_price_100un[i] / 100
    egg_price_un.append(r)

# -----------------------------------------
addit_eggs = []
for i in range(0, n):
    r = cost_addit_hen[i] / egg_price_un[i]
    addit_eggs.append(r)

breakeven = []
egg_production_improv = []

for i in range(0, n):
    r = addit_eggs[i] / x_eggs_hen_total[i] * 100
    breakeven.append(r)

for i in range(0, n):
    r = egg_production_improvement[0]
    egg_production_improv.append(r)

count = 0
for i in range(0, n):
    if breakeven[i] <= egg_production_improv[i]:
        count = count + 1

breakeven_profit_value = egg_production_improvement

breakeven_likel = round(count / n * 100, 1)
print()
print("Summary Report".center(60, "-"))
print(case_name.center(60) + str(todaysdate))
print("-"*60)
print("Number of eggs to be produced to reach breakeven :")
print("Likelihood of 25% -Q1 : ", round(np.percentile(addit_eggs, 75), 1))
print("Likelihood of 50% -Mediam : ", round(np.percentile(addit_eggs, 50), 1))
print("Likelihood of 75% -Q3 : ", round(np.percentile(addit_eggs, 25), 1))
print("-"*60)
print("Laying rate improvement to break-even (%)")
print("Likelihood of 25% - Q1 : ", round(np.percentile(breakeven, 75), 2))
print("Likelihood of 50% - Mediam : ", round(np.percentile(breakeven, 50), 2))
print("Likelihood of 75% - Q3 : ", round(np.percentile(breakeven, 25), 2))
print("-"*60)
print("Likelilhood for make money is: ", breakeven_likel, " %")
print("")
print("------------------- Trikky - v1.0 ----------------" + str(todaysdate))


# charts
# ------------------------------------------
fig = plt.figure(figsize=(10, 7))
fig.patch.set_facecolor(facecolor_chart)
fig.patch.set_alpha(0.7)
gs = GridSpec(nrows=1, ncols=2)

# ------------ Histogram ---------------------
ax1 = fig.add_subplot(gs[0, 0])
ax1.hist(breakeven, bins=40, alpha=chart_alpha)
ax1.set_facecolor(facecolor_chart)
xmin, xmax, ymin, ymax = ax1.axis()

if xmin >= egg_improv:
    egg_improv = xmin
    profitable_msn = ''

if xmax <= egg_improv:
    xmax = egg_improv

# ax1.axvline(egg_improv, color='g', linestyle='dashed', linewidth=2)
ax1.axvline(st.median(breakeven), color='black', linestyle='dotted', linewidth=1, alpha=.7)
ax1.axvline((egg_production_improvement), color='r', linestyle='dashed', linewidth=2)
ax1.set_xlabel("Histogram of egg production for break-even (%)", fontsize=xaxis_font_size)
ax1.set_title("The likelilhood of make money is: " + str(breakeven_likel) + " %", fontsize=12, fontweight='bold')

# paint the background
ax1.axvspan(xmin, egg_improv, facecolor=background_chart_color_profit,
            alpha=background_chart_color_alpha)  # background color
ax1.axvspan(egg_improv, xmax, facecolor=background_chart_color_nonprofit,
            alpha=background_chart_color_alpha)  # background color
ax1.text((egg_improv - xmin) - .05, (ymax + ymin) / 2, profitable_msn, fontsize=7, fontweight='bold')
ax1.set_ylabel("Freq (n) ", fontsize=yaxis_font_size)

# ----------- Boxplot -----------------------------
ax2 = fig.add_subplot(gs[0, 1])
ax2.boxplot(breakeven, showfliers=False, patch_artist=True)
ax2.set_facecolor(facecolor_chart)

xmin2, xmax2, ymin2, ymax2 = ax2.axis()

if ymax2 <= egg_improv:
    ymax2 = egg_improv

if xmax2 >= egg_improv:
    xmax2 = egg_improv
    profitable_msn = ''

ax2.set_ylabel("Egg prod. improv for breakeven (%) ", fontsize=yaxis_font_size)
ax2.set_xlabel("Boxplot", fontsize=xaxis_font_size)
# ax2.axhline(y=egg_improv, color="g", linestyle="dashed", linewidth=2)
ax2.axhline((egg_production_improvement), color='r', linestyle='dashed', linewidth=2)

ax2.axhspan(ymin2, egg_improv, facecolor=background_chart_color_profit,
            alpha=background_chart_color_alpha)  # background color
ax2.axhspan(egg_improv, ymax2, facecolor=background_chart_color_nonprofit,
            alpha=background_chart_color_alpha)  # background color

ax2.text(1.2, egg_improv + 0.005, 'Feed additiv benefit ', fontsize=7)
ax2.text(.6, (egg_improv + ymin2) / 2.1, profitable_msn, fontsize=7, fontweight='bold')
fig.suptitle("Layer break-even  for  " + str(case_name) + str(" - ") + str(todaysdate) + "\n" +
             "Each hen should produce on average +" + str(round(st.median(addit_eggs), 1)) + " eggs in " + str(
    round(st.mean(days_total), 0)) + " days to be profitable", fontsize=10)

plt.savefig(savefigurepath + str(savefigurefilename) + str(case_name) + ".png", dpi=graph_dpi)
plt.show()

# --------------------------------------------------------------------
