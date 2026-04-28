import pandas as pd
import matplotlib.pyplot as plt


def logic_gate_predict(row):
	if row['Sex'] == 'female':
		if row['Pclass'] == 3 and row['Embarked'] == 'S':
			return 0
		else:
			return 1
	elif row['Sex'] == 'male':
		if pd.notna(row['Age']) and row['Age'] < 17 and row['Pclass'] in [1, 2]:
			return 1
		else:
			return 0


def main():
	test_data = pd.read_csv("titanic_data/test.csv")
	predictions = test_data.apply(logic_gate_predict, axis=1)
	output = pd.DataFrame({'PassengerId': test_data['PassengerId'], 'Survived': predictions})
	output.to_csv('my_advanced_logic_submission.csv', index=False)


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
