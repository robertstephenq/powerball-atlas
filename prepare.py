import json,re,html,datetime
from pathlib import Path
p=Path(__file__).parent
s=(p/'media.html').read_text(); records=[]
for row in re.findall(r'<tr[^>]*>(.*?)</tr>',s,re.S):
 cells={k:re.sub('<[^>]+>',' | ',v) for k,v in re.findall(r'<td\s+data-label="([^"]+)"[^>]*>(.*?)</td>',row,re.S)}
 if not all(k in cells for k in ['Winner','Date','Option','Prize']):continue
 parts=[html.unescape(x.strip()) for x in cells['Winner'].split('|') if x.strip()]
 date=' '.join(cells['Date'].replace('.','').split()).replace('Sept ','Sep ')
 try:d=datetime.datetime.strptime(date,'%b %d, %Y').strftime('%Y-%m-%d')
 except ValueError:continue
 money=re.search(r'\$([\d,\.]+)\s*annuity',cells['Prize'])
 if not money or len(parts)<2:continue
 option=' '.join(cells['Option'].split()); winner=' '.join(parts[:-1]);state=parts[-1]
 records.append(dict(date=d,state=state,winner=winner,amount=float(money[1].replace(',','')),split='split' in cells['Prize'],status='Claimed' if option.lower() in ['cash','annuity'] else ('Unclaimed' if 'unclaimed' in (winner+option).lower() else 'Not reported')))
(p/'public/jackpots.json').write_text(json.dumps(records))
print(len(records),'jackpot records;',len(set(r['state'] for r in records)),'states / territories')
