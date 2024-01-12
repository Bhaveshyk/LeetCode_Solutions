select emp.name, bns.bonus 
  from Employee emp left join Bonus bns 
  on emp.empId = bns.empId 
  where bns.bonus < 1000 or bns.bonus is null
