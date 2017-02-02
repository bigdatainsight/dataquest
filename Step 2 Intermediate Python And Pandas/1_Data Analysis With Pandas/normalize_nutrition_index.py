# -*- coding: utf-8 -*-
"""
Created on Mon May 30 22:28:01 2016

@author: eyaneri
"""
import pandas

food_info = pandas.read_csv("food_info.csv")
cols = food_info.columns.tolist()

def normalize_nutrition_index():
    food_info["Normalized_Protein"] = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
    food_info["Normalized_Fat"] = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()
    food_info["Norm_Nutr_Index"] = 2*food_info["Normalized_Protein"] + (-0.75*food_info["Lipid_Tot_(g)"])
    food_info.sort_values("Norm_Nutr_Index", inplace=True, ascending=False)