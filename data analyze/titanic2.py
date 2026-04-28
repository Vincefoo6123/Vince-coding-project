import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def feature_engineering(df):
    # 1. 缺失值處理：Fare 用中位數填補，Embarked 預設為最頻繁的 'S'
    df['Embarked'] = df['Embarked'].fillna('S')
    df['Fare'] = df['Fare'].fillna(df['Fare'].median())
    # 2. 專業特徵提取 ：利用 Regex 從 Name 中提取頭銜
    # 精準捕捉社會地位，例如 'Master' 通常指男童，'Rare' 代表貴族或專業人員
    df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
    df['Title'] = df['Title'].replace(['Lady', 'Countess','Capt', 'Col', 'Don', 'Dr','Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    df['Title'] = df['Title'].replace('Mlle', 'Miss')
    df['Title'] = df['Title'].replace('Ms', 'Miss')
    df['Title'] = df['Title'].replace('Mme', 'Mrs')
    # 3. 進階缺失值填補：不只是填平均值，而是根據「頭銜」分組後填入中位數
    # 確保 'Master' (男孩) 的年齡不會被填成成年人的平均值
    df['Age'] = df.groupby('Title')['Age'].transform(lambda x: x.fillna(x.median()))
    # 4. 創造新變數：FamilySize (家族規模) 與 IsAlone (是否隻身一人)
    # 因數據顯示獨行者與大家庭的生存規律有顯著差異
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
