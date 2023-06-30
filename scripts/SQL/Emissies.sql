SELECT DISTINCT
    y.bu_code,
    y.bu_naam,
	SUM( p.[Fijn stof (PM10)]/ y.distance) as fijnstof_afstand, 
	SUM(  p.[Stikstofoxiden (NOx / NO2)]/ y.distance) as stikstof_afstand
FROM 
(
    SELECT 
        p1.nic, 
        p1.bedrijf,
        p1.[Fijn stof (PM10)], 
        p1.[Stikstofoxiden (NOx / NO2)],
        a.centroid_bedrijf
    FROM
    (
        SELECT 
            [nic], 
            [bedrijf], 
            [emissiestof], 
            [emissie]
        FROM [dbo].[eMJV_EPRTRLucht]
        WHERE jaar = 2020
    ) AS SourceTable
    PIVOT
    (
        MAX([emissie])
        FOR [emissiestof] IN ([Fijn stof (PM10)],[Stikstofoxiden (NOx / NO2)])
    ) AS p1
    JOIN
    (
        SELECT 
            [nic], 
            [bedrijf],
            Geometry::Point([x_Coordinaat], [y_Coordinaat], 28999) as centroid_bedrijf
        FROM [dbo].[eMJV_AlgemeneGegevens]
    ) a ON p1.nic = a.nic
) p
JOIN
(
    SELECT 
        nic, 
        bedrijf, 
        bu_code,
        bu_naam,
	    geom.STCentroid() as centroid_buurt,
	    geom.STCentroid().STDistance(Geometry::Point([x_Coordinaat], [y_Coordinaat], 28992)) AS distance
    FROM [dbo].[CBS_Buurten_2020_Geo], [dbo].[eMJV_AlgemeneGegevens]
    WHERE gm_naam IN ('Amsterdam', 'Haarlemmermeer', 'Zaanstad', 'Aalsmeer', 'Amstelveen', 'Diemen', 'Ouder-Amstel', 'Uithoorn')
        AND geom.STCentroid().STDistance(Geometry::Point([x_Coordinaat], [y_Coordinaat], 28992)) <= 30000
) y ON p.nic = y.nic
group by y.bu_code, y.bu_naam