import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

### Age and Damage Visualization

def visualize_age_and_damage(data):
    # Create age categories
    age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    age_labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']

    # Create a new column to represent age categories for visualization
    data_to_plot = data.copy()  # Create a copy of the original data
    data_to_plot['age_category'] = pd.cut(data_to_plot['age'], bins=age_bins, labels=age_labels)

    # Calculate the count of buildings in each age category
    age_count = data_to_plot['age_category'].value_counts().sort_index()

    # Calculate the percentage of damage sizes for each age category
    age_damage_percentage = data_to_plot.groupby('age_category')['damage_grade'].value_counts(normalize=True).unstack(fill_value=0) * 100

    # Create two subplots side by side
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Plot the count of buildings in each age category
    age_count.plot(kind='bar', ax=axes[0])
    axes[0].set_xlabel('Age Category')
    axes[0].set_ylabel('Number of Buildings')
    axes[0].set_title('Number of Buildings in Each Age Category')

    # Plot the percentage of damage sizes by age category with improved style
    sns.set_palette("Set3")  # Choose a color palette
    age_damage_percentage.plot(kind='bar', stacked=True, ax=axes[1])
    axes[1].set_xlabel('Age Category')
    axes[1].set_ylabel('Percentage of Damage Size')
    axes[1].set_title('Percentage of Damage Size by Age Category')
    axes[1].legend(title='Damage Size', loc='upper right')

    # Add labels to the bars
    for p in axes[1].patches:
        width, height = p.get_width(), p.get_height()
        x, y = p.get_xy()
        axes[1].annotate(f'{height:.2f}%', (x + width / 2, y + height / 2), ha='center', va='center')

    # Show the plots
    plt.tight_layout()
    plt.show()
