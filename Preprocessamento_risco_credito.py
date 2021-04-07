# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 12:23:12 2021

@author: Anderson Lomba
"""

import pandas as pd
base = pd.read_csv('german_credit_data.csv')


base.loc[pd.isnull(base['Conta Poupança'])]
base.loc[pd.isnull(base['Conta corrente'])]


# Apagando coluna de índice a mais
base.drop('ClienteID',axis=1)
base.drop('Índice',axis=1)


pd.get_dummies(base['Objetivo'])
Objetivo = pd.get_dummies(base['Objetivo'])


base.replace(['repairs','vacation/others'],['Reparos','Ferias/Outros'])





