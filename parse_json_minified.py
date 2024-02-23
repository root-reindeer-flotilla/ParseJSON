L='utf-8'
import json,argparse as M
from datetime import datetime as N
from zoneinfo import ZoneInfo as E
D=M.ArgumentParser(description='Parse JSON file and optionally output in Markdown format. Includes an option to only show unknown users.')
D.add_argument('input_file',type=str,help='Input JSON file path')
D.add_argument('-md','--markdown',action='store_true',help='Output in Markdown format')
D.add_argument('-o','--output',type=str,help='Output file name (without extension)')
B=D.parse_args()
O='md'if B.markdown else'txt'
P=f"{B.output}.{O}"if B.output else None
def Q(data_str,output_file):
	B=output_file;A=data_str
	if B:
		with open(B,'a',encoding=L)as C:C.write(A+'\n')
	else:print(A)
with open(B.input_file,'r',encoding=L)as R:
	for S in R:
		A=json.loads(S);F=A.get('sender');G=A.get('text');H=A.get('tokenCount');I=A.get('model');J=A.get('user');C=A.get('updatedAt',{}).get('$date')
		if C:T=N.strptime(C,'%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=E('UTC'));U=T.astimezone(E('America/Detroit'));C=U.strftime('%Y-%m-%d %H:%M:%S')
		if B.markdown:K=f"""**Sender:** {F}  
**User:** {J}  
**Model:** {I}  
**Token Count:** {H}  
**Updated At:** {C}  
**Text:**

{G}

---
"""
		else:K=f"""Sender: {F}
User: {J}
Model: {I}
Token Count: {H}
Updated At: {C}
Text:
{G}

-----
"""
		Q(K,P)