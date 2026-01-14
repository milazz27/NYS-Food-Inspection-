SELECT
    f.fullname,
    f.fid
FROM
    facilities f,
    frequencies fr 
WHERE
    f.fid = fr.fid
    and lower(f.fullname) like '%kebab%'
;

SELECT
    violation_description
FROM
    violation_details d
WHERE
    d.fid = 'aedf63d4-fce1-4839-9636-6fd535deb9b8'
;