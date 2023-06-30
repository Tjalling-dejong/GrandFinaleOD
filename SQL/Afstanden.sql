SELECT 
nic, 
bedrijf, 
  Geometry::Point([x_Coordinaat], [y_Coordinaat], 28992) as centroid_bedrijf,
  bu_code,
  bu_naam,
	  geom.STCentroid() as centroid_buurt,
	  geom.STCentroid().STDistance(Geometry::Point([x_Coordinaat], [y_Coordinaat], 28992)) AS distance
  FROM [dbo].[CBS_Buurten_2020_Geo], [dbo].[eMJV_AlgemeneGegevens]
  WHERE gm_naam IN ('Amsterdam', 'Haarlemmermeer', 'Zaanstad', 'Aalsmeer', 'Amstelveen', 'Diemen', 'Ouder-Amstel', 'Uithoorn');