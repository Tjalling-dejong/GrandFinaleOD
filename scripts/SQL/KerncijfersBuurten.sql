SELECT [regio]
      ,[gm_naam]
      ,[recs]
      ,[gwb_code]
      ,[ind_wbi]
      ,[a_inw] as [Aantal inwoners]
      ,[a_opl_lg] as [Aantal laag opgeleiden]
      ,[a_opl_md] as [Aantal middelbaar opgeleiden] 
      ,[a_opl_hg] as [Aantal hoog opgeleiden]
      ,[g_hh_sti] as [Gem gestandaardiseerd inkomen van huish] 
  FROM [dbo].[CBS_Kerncijfers_Wijken_en_Buurten_2020]
  WHERE recs = 'Buurt'
  AND gm_naam IN ('Amsterdam', 'Haarlemmermeer', 'Zaanstad', 'Aalsmeer', 'Amstelveen', 'Diemen', 'Ouder-Amstel', 'Uithoorn')