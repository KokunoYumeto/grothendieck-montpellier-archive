-- Preserve code text while allowing long source locators to wrap.
function Code(el)
  if FORMAT:match('latex') and not el.text:match('[{}\\%%]') then
    return pandoc.RawInline('latex', '\\nolinkurl{' .. el.text .. '}')
  end
end

function Str(el)
  if FORMAT:match('latex') and #el.text > 28 and
       (el.text:match('%.lean') or el.text:match('%.py') or el.text:match('%.tsv')) and
       not el.text:match('[{}\\%%]') then
    return pandoc.RawInline('latex', '\\nolinkurl{' .. el.text .. '}')
  end
end
