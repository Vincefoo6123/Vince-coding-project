import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def feature_engineering(df):
    df['Embarked'] = df['Embarked'].fillna('S')
    df['Fare'] = df['Fare'].fillna(df['Fare'].median())
    df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
    df['Title'] = df['Title'].replace(['Lady', 'Countess','Capt', 'Col', 'Don', 'Dr','Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    df['Title'] = df['Title'].replace('Mlle', 'Miss')
    df['Title'] = df['Title'].replace('Ms', 'Miss')
    df['Title'] = df['Title'].replace('Mme', 'Mrs')
    df['Age'] = df.groupby('Title')['Age'].transform(lambda x: x.fillna(x.median()))
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['IsAlone'] = 1
    df.loc[df['FamilySize'] > 1, 'IsAlone'] = 0
    features = ['Pclass', 'Sex', 'Age', 'Fare', 'Embarked', 'Title', 'FamilySize', 'IsAlone']
    return df[features]


def main():
    train_data = pd.read_csv("titanic_data/train.csv")
    test_data = pd.read_csv("titanic_data/test.csv")
    train_features = feature_engineering(train_data)
    test_features = feature_engineering(test_data)
    y_train = train_data["Survived"]
    X_train = pd.get_dummies(train_features)
    X_test = pd.get_dummies(test_features)
    X_train, X_test = X_train.align(X_test, join='left', axis=1, fill_value=0)
    model = RandomForestClassifier(n_estimators=200, max_depth=6, in_samples_split=4, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
    output.to_csv('ultimate_submission.csv', index=False)


if __name__ == "__main__":
    main()