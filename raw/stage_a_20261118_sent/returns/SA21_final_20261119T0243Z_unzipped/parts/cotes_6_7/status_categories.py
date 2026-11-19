"""Manually assigned dominant categories after reading the source and each
record.  These are not inferred by keyword matching.  The full status_on_pages
field retains mixed situations, self-corrections and limitations.
"""
STATUS_BY_COTE={
 6: {
 1:'proof sketched',2:'definition/construction',3:'definition/construction',
 4:'corrected by himself later',5:'proof sketched',6:'proof sketched',
 7:'proof sketched',8:'proof sketched',9:'open on the pages',10:'proof sketched',
 11:'corrected by himself later',12:'open on the pages',13:'open on the pages',
 14:'proof sketched',15:'corrected by himself later',16:'false as stated',
 17:'definition/construction',18:'definition/construction',19:'stated without proof',
 20:'proof sketched',21:'definition/construction',22:'proved there',23:'proved there',
 24:'proof sketched',25:'corrected by himself later',26:'proof sketched',
 27:'proof sketched',28:'proof sketched',29:'corrected by himself later',
 30:'definition/construction',31:'corrected by himself later',32:'proof sketched',
 33:'proved there',34:'corrected by himself later',35:'proof sketched',
 36:'open on the pages',37:'definition/construction',38:'open on the pages',
 39:'proved there',40:'stated without proof',41:'stated without proof',
 42:'definition/construction',43:'definition/construction',44:'definition/construction'},
 7: {
 1:'proof sketched',2:'corrected by himself later',3:'proof sketched',
 4:'false as stated',5:'definition/construction',6:'definition/construction',
 7:'corrected by himself later',8:'proved there',9:'corrected by himself later',
 10:'proof sketched',11:'proof sketched',12:'definition/construction',
 13:'open on the pages',14:'proof sketched',15:'corrected by himself later',
 16:'stated without proof',17:'false as stated',18:'corrected by himself later',
 19:'open on the pages',20:'proved there',21:'proof sketched',22:'proved there',
 23:'proved there',24:'stated without proof',25:'open on the pages',
 26:'definition/construction',27:'definition/construction',28:'proved there',
 29:'proof sketched',30:'proof sketched',31:'open on the pages',
 32:'corrected by himself later',33:'proof sketched',34:'open on the pages',
 35:'corrected by himself later',36:'definition/construction',37:'definition/construction',
 38:'proved there',39:'proved there',40:'proof sketched',41:'proved there',
 42:'proof sketched',43:'corrected by himself later',44:'proved there',
 45:'false as stated',46:'proof sketched',47:'proof sketched',48:'proof sketched',
 49:'proof sketched',50:'definition/construction',51:'definition/construction',
 52:'proof sketched'}
}
STATUS_CATEGORIES={f'C-SA21-{cote}-{n:03d}':status for cote,rows in STATUS_BY_COTE.items() for n,status in rows.items()}
