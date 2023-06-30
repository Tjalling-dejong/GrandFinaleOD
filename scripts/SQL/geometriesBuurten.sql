SELECT [qgs_fid]
      ,[geom]
      ,[bu_code]
      ,[bu_naam]
      ,[wk_code]
      ,[gm_code]
      ,[gm_naam]
  FROM [dbo].[CBS_Buurten_2020_Geo]
  WHERE gm_naam IN ('Amsterdam', 'Haarlemmermeer', 'Zaanstad', 'Aalsmeer', 'Amstelveen', 'Diemen', 'Ouder-Amstel', 'Uithoorn');