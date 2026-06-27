DATA PREPROCESSING

*data preprocessing is the first part of ml pipeline.
*data is refined so that we can train the model easly and efficiently.
1.Duplicate
  if the data are accidental
    remove the row
  else
    keep
2.Missing values
  if the missing values are fewer/less
    remove it
  else
    apply imputation
3.Label encoding vs One-Hot encoding
  if the data shows some order ->label encoding
   eg:small,medium,large,xl,xxl
      constable,SI,CI,commissioner
  if the data shows any order ->One-Hot encoding
   eg:car,bike,fruits,etc

 Key Points

• Missing values reduce data quality.
• Duplicate records can bias the model.
• Data preprocessing is done before training.
• Label Encoding → Ordered data.
• One-Hot Encoding → Unordered data.                 