{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f1324ebd-d538-4b80-8b41-a1919e02958a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Figure size 1000x600 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 1000x600 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "from datetime import date, timedelta\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "\n",
    "# Générer des données factices\n",
    "def generate_fake_data():\n",
    "    vehicles = ['Voiture', 'Moto', 'Camionnette']\n",
    "    services = ['Vérification', 'Réparation moteur', 'Carrosserie', 'Panneau solaire']\n",
    "    \n",
    "    data = []\n",
    "    for i in range(30):\n",
    "        date_ = (date.today() - timedelta(days=30-i)).strftime('%Y-%m-%d')\n",
    "        vehicle = np.random.choice(vehicles)\n",
    "        service = np.random.choice(services)\n",
    "        hours = np.random.randint(1, 5)\n",
    "        cost = round(np.random.uniform(200, 800), 2)\n",
    "        \n",
    "        data.append([date_, vehicle, service, hours, cost])\n",
    "    \n",
    "    df = pd.DataFrame(data, columns=['Date', 'Type_Véhicule', 'Prestation', 'Heures', 'Coût'])\n",
    "    return df\n",
    "\n",
    "# Analyse croisée véhicule/préparation\n",
    "def cross_analysis(df):\n",
    "    pivot = df.pivot_table(index='Type_Véhicule', columns='Prestation', values='Coût', aggfunc='mean')\n",
    "    plt.figure(figsize=(10,6))\n",
    "    sns.heatmap(pivot, annot=True, cmap='YlGnBu')\n",
    "    st.pyplot()\n",
    "\n",
    "# Calcul du taux horaire\n",
    "def hourly_rate(df):\n",
    "    rate = df['Coût'] / df['Heures']\n",
    "    return round(rate.mean(), 2)\n",
    "\n",
    "# KPIs avancés\n",
    "def display_kpis(df):\n",
    "    total_revenue = df['Coût'].sum()\n",
    "    avg_prestation = df['Coût'].mean()\n",
    "    piece_ratio = np.random.uniform(0.3, 0.7) # Valeur factice\n",
    "    margin = round(np.random.uniform(0.25, 0.4), 2)\n",
    "    \n",
    "    st.markdown(f\"**Chiffre d'affaires total : {total_revenue}€**\")\n",
    "    st.markdown(f\"**Montant moyen par prestation : {avg_prestation}€**\")\n",
    "    st.markdown(f\"**Ratio pièces/main d'œuvre : {piece_ratio:.2f}**\")\n",
    "    st.markdown(f\"**Marge moyenne par prestation : {margin*100}%**\")\n",
    "\n",
    "# Prévisions et tendances\n",
    "def trends_analysis(df):\n",
    "    df['Date'] = pd.to_datetime(df['Date'])\n",
    "    daily_revenue = df.groupby('Date')['Coût'].sum().reset_index()\n",
    "    \n",
    "    # Moyenne mobile sur 7 jours\n",
    "    daily_revenue['Moyenne Mobile'] = daily_revenue['Coût'].rolling(7).mean()\n",
    "    \n",
    "    plt.figure(figsize=(10,6))\n",
    "    plt.plot(daily_revenue['Date'], daily_revenue['Coût'], label='CA Journalier')\n",
    "    plt.plot(daily_revenue['Date'], daily_revenue['Moyenne Mobile'], label='Moyenne Mobile 7j', linestyle='--')\n",
    "    plt.legend()\n",
    "    st.pyplot()\n",
    "\n",
    "# Fonction principale\n",
    "def main():\n",
    "    st.title(\"Suivi d'activité du garage automobile\")\n",
    "    \n",
    "    # Charger les données factices\n",
    "    df = generate_fake_data()\n",
    "    \n",
    "    # Analyse croisée véhicule/préparation\n",
    "    st.header(\"Analyse croisée véhicule/préparation\")\n",
    "    cross_analysis(df)\n",
    "    \n",
    "    # KPIs avancés\n",
    "    st.header(\"KPIs avancés\")\n",
    "    display_kpis(df)\n",
    "    \n",
    "    # Prévisions et tendances\n",
    "    st.header(\"Prévisions et tendances\")\n",
    "    trends_analysis(df)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "1a7554c8-b26a-4f96-b080-710837f4185f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
