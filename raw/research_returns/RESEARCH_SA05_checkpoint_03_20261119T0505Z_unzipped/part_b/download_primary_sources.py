import urllib.request
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from time import monotonic
import hashlib,json
root=Path('/workspace/scratch/6215ed17d0f0/primary_sources/part_b');root.mkdir(parents=True,exist_ok=True)
items=[
('bloch_kato1990.pdf','https://math.stanford.edu/~conrad/BSDseminar/refs/BKTamagawa.pdf'),
('flach_morin2018.pdf','https://ems.press/content/serial-article-files/26429?nt=1'),
('geisser2004.pdf','https://arxiv.org/pdf/math/0404425'),
('milne2006.pdf','https://www.jmilne.org/math/Books/ADTnot.pdf'),
('kurihara1992.pdf','https://www.numdam.org/item/CM_1992__81_2_223_0.pdf'),
('rognes_weibel.pdf','https://sites.math.rutgers.edu/~weibel/archive/papers-dir/RognesWeibel.pdf'),
('milne_addendum2025.pdf','https://www.jmilne.org/math/Books/add/ADT2006.pdf'),
('borel1974.pdf','https://www.numdam.org/article/ASENS_1974_4_7_2_235_0.pdf'),
('scholbach2015.pdf','https://arxiv.org/pdf/1003.1219'),
('lichtenbaum2005.pdf','https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E70A59FA79C01CDBCD940699A72A6F59/S0010437X04001150a.pdf/the-weil-etale-topology-on-schemes-over-finite-fields.pdf'),
('lichtenbaum2009.pdf','https://annals.math.princeton.edu/wp-content/uploads/annals-v170-n2-p05-p.pdf'),
('geisser_schmidt2018.pdf','https://www.mathi.uni-heidelberg.de/~schmidt/papers/poitou-highdim.pdf'),
('gonzalez_tan2006.pdf','https://arxiv.org/pdf/math/0608587'),
('keller2019.pdf','https://ems.press/content/serial-article-files/26477?nt=1'),
('chen_partial_vandiver2026.pdf','https://arxiv.org/pdf/2602.05090'),
('keller2016.pdf','https://www.timo-keller.de/articles/TateShafarevich.pdf'),
('keller2021.pdf','https://www.timo-keller.de/articles/Shap.pdf'),
('qin2024.pdf','https://link.springer.com/content/pdf/10.1007/s00209-024-03487-8.pdf'),
('yuan2020.pdf','https://arxiv.org/pdf/2011.12897'),
('tate1966.pdf','https://pazuki.perso.math.cnrs.fr/index_fichiers/Tate66.pdf'),
('balkan_schreieder2026.pdf','https://link.springer.com/content/pdf/10.1007/s00029-026-01142-0.pdf'),
('fontaine1992.pdf','https://www.imo.universite-paris-saclay.fr/~fontaine/bourbakiblochkato.pdf'),
('voevodsky2011.pdf','https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Voe-mot.pdf'),
('geisser_dedekind2004.pdf','https://www2.rikkyo.ac.jp/web/geisser/Dedekind.pdf'),
('kahn2003.pdf','https://www.numdam.org/item/ASENS_2003_4_36_6_977_0.pdf'),
('conrad2006.pdf','https://math.stanford.edu/~conrad/papers/Kktrace.pdf'),
('dejong1996.pdf','https://www.numdam.org/item/PMIHES_1996__83__51_0.pdf'),
('deligne1968.pdf','https://www.numdam.org/item/PMIHES_1968__35__107_0.pdf'),
('milne1999.pdf','https://www.jmilne.org/math/articles/1999bP.pdf'),
('vanhoften_sempliner2026.pdf','https://polvanhoften2.github.io/Pol%20van%20Hoften%20and%20Jack%20Sempliner%20-%20The%20Hodge%20conjecture%20for%20CM%20abelian%20varieties.pdf'),
('kerr_yang2018.pdf','https://msp.org/akt/2018/3-2/akt-v3-n2-p01-p.pdf'),
('kerr_li2020.pdf','https://msp.org/pjm/2020/306-2/pjm-v306-n2-p06-p.pdf'),
('collins1975.pdf','https://link.springer.com/content/pdf/10.1007/3-540-07407-4_17.pdf'),
('basu_survey2014.pdf','https://www.math.purdue.edu/~sbasu/raag_survey2011_final-sep4-2014.pdf'),
('seidenberg1974.pdf','https://scispace.com/pdf/constructions-in-algebra-3zcc352k1e.pdf'),
('ferrand2003.pdf','https://www.numdam.org/item/BSMF_2003__131_4_553_0.pdf'),
('bhatt2016.pdf','https://arxiv.org/pdf/1404.7483'),
('besser_dejeu2003.pdf','https://www.numdam.org/article/ASENS_2003_4_36_6_867_0.pdf'),
('sakugawa2021.pdf','https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B08F41641AF6FEE54CED590D02D5288B/S0008414X20000073a.pdf/generalized-beilinson-elements-and-generalized-soule-characters.pdf'),
('scholbach_special2017.pdf','https://jakobscholbach.github.io/reprints/Special%20L-values%20of%20geometric%20motives.pdf'),
('adrien_morin2024.pdf','https://arxiv.org/pdf/2411.07896')]
def get(item):
 name,url=item;t=monotonic()
 try:
  if (root/name).exists():
   data=(root/name).read_bytes()
   if not data.startswith(b'%PDF'): raise ValueError('Existing file is not a PDF')
   return dict(name=name,url=url,size=len(data),sha256=hashlib.sha256(data).hexdigest(),status='already present')
  data=urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'}),timeout=45).read()
  if not data.startswith(b'%PDF'): raise ValueError('Endpoint did not return a PDF')
  (root/name).write_bytes(data)
  return dict(name=name,url=url,size=len(data),seconds=round(monotonic()-t,3),sha256=hashlib.sha256(data).hexdigest(),status='downloaded')
 except Exception as e:return dict(name=name,url=url,seconds=round(monotonic()-t,3),status=str(e))
with ThreadPoolExecutor(max_workers=4) as ex: results=list(ex.map(get,items))
print(json.dumps(results,indent=2));(root/'download_log.json').write_text(json.dumps(results,indent=2))
