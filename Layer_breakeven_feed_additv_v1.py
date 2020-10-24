# Guilherme - Jun 2019
# Breakeven - Layers - V - beta .95
# with graph interfacce -Oct. 23th 2020
# tringular density function
import os
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import random as rd
import statistics as st
import time
import numpy as np
from tkinter import *

# definition of screen parameters
screen_x = int(500)
screen_y = int(400)
x_pos = int(50)
y_pos = int(50)
entry_char= int(10)

# -------------------------------------------------------------
# ------------------ input parameters -------------------------
# -------------------------------------------------------------
# define input variables - sequence: min, max, most probably
#


def run_simul() :
    global inputed_scr_farm_ident
    inputed_scr_farm_ident = str(scr_farm_ident.get())
    scr_farm_box.delete(0,END)

    global inputed_egg_price_min
    inputed_egg_price_min = float(scr_egg_price_min.get())
    scr_egg_price_box_min.delete(0,END)
    
    global inputed_egg_price_max
    inputed_egg_price_max = float(scr_egg_price_max.get())
    scr_egg_price_box_max.delete(0,END)

    global inputed_egg_price_mp
    inputed_egg_price_mp = float(scr_egg_price_mp.get())
    scr_egg_price_box_mp.delete(0,END)
    
    global inputed_egg_prod_min
    inputed_egg_prod_min = float(scr_egg_prod_min.get())
    scr_egg_prod_box_min.delete(0,END)

    global inputed_egg_prod_max
    inputed_egg_prod_max = float(scr_egg_prod_max.get())
    scr_egg_prod_box_max.delete(0,END)

    global inputed_egg_prod_mp
    inputed_egg_prod_mp = float(scr_egg_prod_mp.get())
    scr_egg_prod_box_mp.delete(0,END)
    
    global inputed_scr_adit_price
    inputed_scr_adit_price = float(scr_adit_price.get())
    scr_adit_price_box.delete(0,END)

    global inputed_scr_aditiv_incl
    inputed_scr_aditiv_incl = float(scr_aditiv_incl.get())
    scr_aditiv_incl_box.delete(0,END)
    
    global inputed_egg_improv
    inputed_egg_improv = float(scr_egg_improv.get())
    scr_egg_improv_box.delete(0,END)

    
    period_weeks = [100]
    #print(inputed_egg_prod_min)
    eggs_hen_total = [inputed_egg_prod_min, inputed_egg_prod_max, inputed_egg_prod_mp]  # min , max & MP
    print(eggs_hen_total)
    feed_price = [300, 500, 450]  # $$$ - min , max & MP
    
    egg_price_100un = [inputed_egg_price_min, \
                       inputed_egg_price_max, \
                       inputed_egg_price_mp]  # % values
    
    addit_price_kg = [inputed_scr_adit_price]  # $$$ / kg of feed aditive
    inclusion_ton = [inputed_scr_aditiv_incl]  # kg / ton of feed
    
    feed_cons_day = [.1]  # 100g / day / hen
    case_name = "customer_name"  # customer name
    savefigurepath = os.path.dirname(os.path.realpath(__file__))
    
    # savefigurepath = "/Users/Usuario/Desktop/python/" # folder path to store the chart figure (output)
    savefigurefilename = "/layer_case_"  # name of the file of the output
    graph_dpi = 200  # resolution of chart in dpi
    
    egg_production_improvement = [inputed_egg_improv / 100]  # (%) expected improvement with probiotc
    breakevenprob_profit_percent = 75  # (%) - probability of the break-even from up is considered profitable area (number from 0 to 100)
    
    n = 20000  # number of repetitions - ideal 10K or more
    
    ##################################################################
    # facecolor_chart = '#E0E0E0'
    facecolor_chart = '#ffffff'
    background_chart_color_profit = "#a8e6cf"
    background_chart_color_nonprofit = "#ffbaba"
    background_chart_color_alpha = .4
    chart_alpha = .9
    
    xaxis_font_size = 7
    yaxis_font_size = 7
    
    profitable_msn = "Profitable Region"
    
    todaysdate = time.strftime("%d/%m/%Y")
    egg_produ_improv = egg_production_improvement[0]
    egg_improv = egg_production_improvement[0]
    
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
        r = x_feed_cons_day[i] * 100 * 7
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
    print(inputed_scr_farm_ident.center(60) + str(todaysdate))
    print("-" * 60)
    print("Number of eggs to be produced to reach breakeven :")
    print("Likelihood of 25% -Q1 : ", round(np.percentile(addit_eggs, 75), 1))
    print("Likelihood of 50% -Mediam : ", round(np.percentile(addit_eggs, 50), 1))
    print("Likelihood of 75% -Q3 : ", round(np.percentile(addit_eggs, 25), 1))
    print("-" * 60)
    print("Laying rate improvement to break-even (%)")
    print("Likelihood of 25% - Q1 : ", round(np.percentile(breakeven, 75), 2))
    print("Likelihood of 50% - Mediam : ", round(np.percentile(breakeven, 50), 2))
    print("Likelihood of 75% - Q3 : ", round(np.percentile(breakeven, 25), 2))
    print("-" * 60)
    print("Likelilhood to be above break-even is: ", breakeven_likel, " %")
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
    ax1.set_title("Likelilhood to be above break-even is: " + str(breakeven_likel) + " %", fontsize=12, fontweight='bold')
    
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
    fig.suptitle("Layer break-even  for  " + str(inputed_scr_farm_ident) + str(" - ") + str(todaysdate) + "\n" +
                 "Each hen should produce on average +" + str(round(st.median(addit_eggs), 1)) + " eggs in 700 days to be profitable", fontsize=10)
    
    plt.savefig(savefigurepath + str(savefigurefilename) + str(inputed_scr_farm_ident) + ".png", dpi=graph_dpi)
    plt.show()
    









screen = Tk()

## Screen Labels

screen.title("Break-Even Estimator for feed aditives - Egg Producers")
screen.geometry('{}x{}'.format(screen_x,screen_y))
lbl_descrip = Label(screen, text = 'Input the data')
lbl_descrip.place(x = x_pos, y = y_pos)

lbl_case = Label(screen, text = 'Farm ident :')
lbl_case.place(x = x_pos, y = y_pos - 20)

lbl_egg_price = Label(screen, text = 'Egg Price (100 un) :')
lbl_egg_price.place(x = x_pos, y = y_pos + 40)

lbl_egg_prod = Label(screen, text = 'Eggs / Layer :')
lbl_egg_prod.place(x = x_pos, y = y_pos + 60)

lbl_adit_price = Label(screen, text = 'Feed Aditiv. Price (kg) :')
lbl_adit_price.place(x = x_pos, y = y_pos + 100)

lbl_adit_incl = Label(screen, text = 'Feed Aditiv. / ton (g) :')
lbl_adit_incl.place(x = x_pos, y = y_pos + 120)

lbl_egg_improv = Label(screen, text = 'Improv.egg with aditiv. :')
lbl_egg_improv.place(x = x_pos, y = y_pos + 140)

##### min   max  mode #####

lbl_egg_improv = Label(screen, text = 'min.')
lbl_egg_improv.place(x = x_pos + 130 + entry_char/1.5, y = y_pos + 20)

lbl_egg_improv = Label(screen, text = 'max.')
lbl_egg_improv.place(x = x_pos + 130 + 80 + entry_char/1.5, y = y_pos + 20)

lbl_egg_improv = Label(screen, text = 'mode')
lbl_egg_improv.place(x = x_pos + 130 + 80 + 80 + entry_char/1.5, y = y_pos + 20)

##########################
# variables

scr_farm_ident = StringVar()
scr_farm_box = Entry(textvariable = scr_farm_ident, width=entry_char + 5)
scr_farm_box.place(x = x_pos + 133 , y = y_pos - 20)

scr_egg_price_min = StringVar()
scr_egg_price_box_min = Entry(textvariable = scr_egg_price_min,  width=entry_char)
scr_egg_price_box_min.place(x = x_pos + 133, y = y_pos + 40)

scr_egg_price_max = StringVar()
scr_egg_price_box_max = Entry(textvariable = scr_egg_price_max,  width=entry_char)
scr_egg_price_box_max.place(x = x_pos + 133 + 78, y = y_pos + 40)

scr_egg_price_mp = StringVar()
scr_egg_price_box_mp = Entry(textvariable = scr_egg_price_mp,  width=entry_char)
scr_egg_price_box_mp.place(x = x_pos + 133 + 78 + 78, y = y_pos + 40)

scr_egg_prod_min = StringVar()
scr_egg_prod_box_min = Entry(textvariable = scr_egg_prod_min, width=entry_char)
scr_egg_prod_box_min.place(x = x_pos + 133, y = y_pos + 60)

scr_egg_prod_max = StringVar()
scr_egg_prod_box_max = Entry(textvariable = scr_egg_prod_max, width=entry_char)
scr_egg_prod_box_max.place(x = x_pos + 133 + 78, y = y_pos + 60)

scr_egg_prod_mp = StringVar()
scr_egg_prod_box_mp = Entry(textvariable = scr_egg_prod_mp, width=entry_char)
scr_egg_prod_box_mp.place(x = x_pos + 133 + 78 + 78, y = y_pos + 60)


scr_adit_price = StringVar()
scr_adit_price_box = Entry(textvariable = scr_adit_price, width=entry_char)
scr_adit_price_box.place(x = x_pos + 133, y = y_pos + 100)

scr_aditiv_incl = StringVar()
scr_aditiv_incl_box = Entry(textvariable = scr_aditiv_incl, width=entry_char)
scr_aditiv_incl_box.place(x = x_pos + 133, y = y_pos + 120)

scr_egg_improv = StringVar()
scr_egg_improv_box = Entry(textvariable = scr_egg_improv, width=entry_char)
scr_egg_improv_box.place(x = x_pos + 133, y = y_pos + 160)

run_button = Button(screen, text='*** Run ***', command = run_simul)
run_button.place(x = x_pos, y = y_pos+200)

screen.mainloop()


# --------------------------------------------------------------------




