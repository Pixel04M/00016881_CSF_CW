import pandas as pd
import matplotlib.pyplot as plt


##### Reading the Dataset
def read_dataset(s):
    dataset = pd.read_csv('D:\CW CS\Student_Performance.csv')
    return dataset


# Data Exploration
def explore_dataset(dataset):
    num_rows, num_columns = dataset.shape
    features = dataset.columns
    sample_data = dataset.head()

    print(f"Number of Rows: {num_rows}")
    print(f"Number of Columns: {num_columns}")
    print("Features:", features)
    print("Sample Data:")
    print(sample_data)



### Finding MINAMAL AND MAXIMAL VALUEs
def min_max(dataset):
    min_performance = dataset['Performance Index'].min()
    max_performance = dataset['Performance Index'].max()
    print(f"Minimum Performance Index: {min_performance}")
    print(f"Maximum Performance Index: {max_performance}")
##Counting  occurrences of 'Yes' and 'No' in Extracurricular Activities
def  count_occurrences_of_yes_and_no(dataset):
    extracurricular_counts = dataset['Extracurricular Activities'].value_counts()
    print("Extracurricular Activities Counts:")
    print(extracurricular_counts)
##  Group data by 'Extracurricular Activities' and calculate summary statistics
def extracurricular_activities_summary_statistics(dataset):
    group_by_activities = dataset.groupby('Extracurricular Activities')
    summary_statistics = group_by_activities['Hours Studied'].describe()
    print("Summary Statistics for Hours Studied by Extracurricular Activities:")
    print(summary_statistics)
#    Plot a histogram of Hours Studied
def histogram(dataset):
    dataset['Hours Studied'].plot.hist(bins=20, edgecolor='k')
    plt.xlabel('Hours Studied')
    plt.ylabel('Frequency')
    plt.title('Distribution of Hours Studied')
    plt.show()
# Task 5: Command Line Interface (CLI)
def main():
    file_path = '\Student_Performance.csv'
    dataset = read_dataset('D:\CW CS\Student_Performance.csv')

    while True:
        print("\nOptions:")
        print("1.Calculate average of studied")
        print("2.Min and Max Index ")
        print("3.Count  occurrences of 'Yes' and 'No' in Extracurricular Activities")
        print("4.Group data by 'Extracurricular Activities' and calculate summary statistics")
        print("5.Show a histogram of Hours Studied  ")
        print("6.Explore Dataset")
        print("7.Clean dataset")
        print("0. Exit ")


        choice = input("Enter your choice (1/2/3/4/5/6/7/): ")

        if choice == '1':
            calculate_average_hours_studied(dataset)
        elif choice == '2':
            min_max(dataset)
        elif choice == '3':
            count_occurrences_of_yes_and_no(dataset)
        elif choice == '4':
            extracurricular_activities_summary_statistics(dataset)
        elif choice == '5':
            histogram(dataset)
        elif choice == '6':
            explore_dataset(dataset)
        elif choice == '7':
            dataset = clean_dataset(dataset)
            print("Dataset Cleaned")

        elif choice == '0':
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
