SELECT
    f.fullname,
    f.fid
FROM
    facilities f,
    frequencies fr 
WHERE
    f.fid = fr.fid
    and lower(f.fullname) like '%jail%'
;

SELECT
    violation_description
FROM
    violation_details d
WHERE
    d.fid = 'd1c58ab6-6170-4188-8068-9611838c8888'
;