"""Follow the six-page public Jubilee catalogue through observed anchors.

Reuse the saved pagination implementation with a different actually queried
term and distinct source/output filenames. No article content is fetched.
"""
import pathlib

root = pathlib.Path(__file__).resolve().parents[1]
source = root / 'code/part_c_pfluger_tdl_inventory.py'
program = source.read_text().replace('Mathematical', 'Jubilee')
program = program.replace('part_c_pfluger_tdl_mathematical.html',
                          'part_c_pfluger_tdl_jubilee.html')
program = program.replace('part_c_pfluger_tdl_page_', 'part_c_pfluger_tdl_jubilee_page_')
program = program.replace('part_c_pfluger_tdl_inventory_output.json',
                          'part_c_pfluger_tdl_jubilee_inventory_output.json')
namespace = {'__name__': '__main__', '__file__': str(source)}
exec(compile(program, str(source), 'exec'), namespace)
