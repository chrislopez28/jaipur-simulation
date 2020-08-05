"""Script to simulate Jaipur opening hand deals"""
import jaipur
import pandas as pd

n_runs = int(input("Enter the number of runs (i.e. 5-card hands to be drawn): "))

def create_starting_hands(n_runs: int, print_hands: bool = False) -> pd.DataFrame:
    print("\nCreating Decks...")
    Decks = [jaipur.Deck() for i in range(n_runs)]

    print("\nDrawing Hands...")
    Hands = [jaipur.Hand() for i in range(n_runs)]

    simulation_data = []
    for i, D in enumerate(Decks):
        D.deal_hand(Hands[i])
        simulation_data.append(Hands[i].summarize())
        if print_hands:
            print("Hand", i + 1, ":", Hands[i].summarize())

    df = pd.DataFrame(simulation_data)
    print("\nSummary of hands generated. The table below shows the number of hands that had 0, 1, 2, 3, 4, or 5 cards of a card type. Each column should add up to the number of simulated hands.\n")
    print(df.apply(pd.value_counts))
    return df

create_starting_hands(n_runs)
