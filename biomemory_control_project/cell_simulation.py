import random
import pandas as pd

BASES = ["A", "T", "C", "G"]


def mutate_dna(dna: str, mutation_rate: float) -> tuple[str, int]:
    mutated = []
    mutation_count = 0

    for base in dna:
        if random.random() < mutation_rate:
            choices = [b for b in BASES if b != base]
            mutated.append(random.choice(choices))
            mutation_count += 1
        else:
            mutated.append(base)

    return ''.join(mutated), mutation_count


def simulate_cell_divisions(
    initial_dna: str,
    divisions: int = 10,
    mutation_rate: float = 0.02,
    growth_multiplier: float = 1.2
) -> pd.DataFrame:
    current_dna = initial_dna
    total_mutations = 0
    cell_count = 1
    records = []

    for division in range(1, divisions + 1):
        current_dna, new_mutations = mutate_dna(current_dna, mutation_rate)
        total_mutations += new_mutations
        cell_count = int(cell_count * growth_multiplier) + 1

        observed_mutation_rate = total_mutations / max(len(initial_dna), 1)

        records.append({
            "division": division,
            "cell_count": cell_count,
            "new_mutations": new_mutations,
            "total_mutations": total_mutations,
            "observed_mutation_rate": observed_mutation_rate,
            "dna_snapshot": current_dna[:80] + ("..." if len(current_dna) > 80 else "")
        })

    return pd.DataFrame(records)
