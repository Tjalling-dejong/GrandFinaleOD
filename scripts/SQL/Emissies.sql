DECLARE @cols AS NVARCHAR(MAX)
DECLARE @query AS NVARCHAR(MAX)

SET @cols = STUFF(
    (
        SELECT DISTINCT ', [' + [emissiestof] + ']'
        FROM [dbo].[eMJV_EPRTRLucht]
        WHERE jaar = 2020
        FOR XML PATH(''), TYPE
    ).value('.', 'NVARCHAR(MAX)'),
    1, 2, ''
)

SET @query = '
    SELECT [nic], [bedrijf], ' + @cols + '
    FROM
    (
        SELECT [nic], [bedrijf], [emissiestof], [emissie]
        FROM [dbo].[eMJV_EPRTRLucht]
        WHERE  jaar = 2020
    ) AS SourceTable
    PIVOT
    (
        MAX([emissie])
        FOR [emissiestof] IN (' + @cols + ')
    ) AS PivotTable'

EXECUTE(@query)