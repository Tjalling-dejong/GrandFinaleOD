  SELECT DISTINCT nic
      ,[bedr_Id]
      ,[bedrijf]
      ,[x_Coordinaat]
      ,[y_Coordinaat]
      ,[n_Coordinaat]
      ,[o_Coordinaat]
  FROM [dbo].[eMJV_AlgemeneGegevens]
  WHERE nic IN (
    SELECT DISTINCT nic 
    FROM [dbo].[eMJV_EPRTRLucht] 
    WHERE [jaar] = 2020
    AND emissiestof IN ('Fijn stof (PM10)', 'Stikstofoxiden (NOx / NO2)'))
 