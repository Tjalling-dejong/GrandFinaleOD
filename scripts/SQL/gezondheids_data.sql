SELECT *
FROM
(
    SELECT DISTINCT
        e.bu_code,
        CASE
            WHEN leeftijd = 20300 THEN '18 jaar of ouder'
            WHEN leeftijd = 53115 THEN '18 - 65 jaar'
            WHEN leeftijd = 80200 THEN '65 jaar of ouder'
        END AS leeftijd_cat,
        g.[ErvarenGezondheidGoedZeerGoed_4]
    FROM
    (
        SELECT DISTINCT
            bu_code
        FROM [dbo].[CBS_Buurten_2020_Geo]
        WHERE gm_naam IN ('Amsterdam', 'Haarlemmermeer', 'Zaanstad', 'Aalsmeer', 'Amstelveen', 'Diemen', 'Ouder-Amstel', 'Uithoorn')
    ) e
    INNER JOIN
    (
        SELECT DISTINCT
            [WijkenEnBuurten],
            leeftijd,
            Marges,
            [ErvarenGezondheidGoedZeerGoed_4]
        FROM [dbo].[RIVM_Ervaren_Gezondheid_2012_2016_2020]
        WHERE LEFT([Perioden], 4) = '2020'
            AND LEFT([WijkenEnBuurten], 2) = 'BU'
            AND Marges = 'MW00000'
    ) g ON e.bu_code = g.[WijkenEnBuurten]
) src
PIVOT
(
    MAX([ErvarenGezondheidGoedZeerGoed_4])
    FOR leeftijd_cat IN ([18 jaar of ouder], [18 - 65 jaar], [65 jaar of ouder])
) pivoted_data;