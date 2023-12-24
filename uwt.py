### Minified using https://python-minifier.com to increase speed. ###
### To view clean source, view [uwt (documented).py]. ###



_I='Windows'
_H='Darwin'
_G='warn'
_F='success'
_E='error'
_D=None
_C=True
_B=False
_A='info'
import discord,aiohttp,asyncio,platform
from pystyle import Colors,Center
import time,os,re,json
class Utilities:
	def log(self,log_type,message,should_print=_C):
		'Log messages with different types.\n\n        Args:\n            log_type (str): Type of log message (info, warn, success, error).\n            message (str): The log message.\n            should_print (bool, optional): Whether to print the log message. Defaults to True.\n\n        Raises:\n            ValueError: If an invalid log type is provided.\n\n        Returns:\n            str: The formatted log message.\n        ';options={_A:f"{Colors.gray}[{Colors.blue}!{Colors.gray}]{Colors.reset}",_G:f"{Colors.gray}[{Colors.yellow}?{Colors.gray}]{Colors.reset}",_F:f"{Colors.gray}[{Colors.green}+{Colors.gray}]{Colors.reset}",_E:f"{Colors.gray}[{Colors.red}-{Colors.gray}]{Colors.reset}"}
		if log_type not in options:raise ValueError('Invalid type for logging.')
		output=f"{options[log_type]} {Colors.gray}[{Colors.reset}{time.strftime('%H:%M:%S')}{Colors.gray}]{Colors.reset}: {message}"
		if should_print:print(output);return
		else:return output
	def clear(self,message=_D):
		'Clear the console screen.\n\n        Args:\n            message (str, optional): Message to print after clearing. Defaults to None.\n\n        Raises:\n            RuntimeError: If clearing the screen is not supported on the current system.\n        ';system=platform.system()
		if system in['Linux',_H]:os.system('clear')
		elif system==_I:os.system('cls')
		else:raise RuntimeError(f"Clearing the screen is not supported on {system}.")
		if message:print(message)
	def title(self,title=_D):
		'Set the terminal title on various platforms.\n\n        Args:\n            title (str): The new title for the terminal.\n\n        Raises:\n            RuntimeError: If setting the terminal title is not supported on the current system.\n        ';system=platform.system()
		if system==_I:os.system(f"title {title}")
		elif system in['Linux',_H]:print(f"]0;{title}\a",end='',flush=_C)
		else:0
	def menu(self,*args):
		'Create a text menu.\n\n        Returns:\n            tuple: A tuple containing the formatted text menu and a list of menu items.\n        ';text=''
		for(i,arg)in enumerate(args):
			if i!=len(args)-1:text+=f"{Colors.gray}[{Colors.green}{i+1}{Colors.gray}]{Colors.reset}: {arg}\n"
			else:text+=f"\n{Colors.gray}[{Colors.red}0{Colors.gray}]{Colors.reset}: {arg}"
		text=text.strip();return text,list(args)
class WHT:
	def __init__(self,webhook_url):'Initialize the WHT class with a Discord webhook URL.\n\n        Args:\n            webhook_url (str): Discord webhook URL.\n        ';self.webhook_url=webhook_url
	async def send(self,**kwargs):
		'Send a message to the Discord webhook.\n\n        Returns:\n            tuple: A tuple containing a boolean indicating success and an error message (if any).\n        '
		try:
			async with aiohttp.ClientSession()as session:webhook=discord.Webhook.from_url(self.webhook_url,session=session);await webhook.send(**kwargs)
			return _C,_D
		except Exception as e:return _B,e
	async def validate(self,webhook_url=_D):
		'Validate a Discord webhook URL.\n\n        Args:\n            webhook_url (str, optional): Discord webhook URL to validate. Defaults to None.\n\n        Returns:\n            bool: True if the URL is valid, False otherwise.\n        ';webhook_url=webhook_url or self.webhook_url
		if not re.compile('^https://(?:ptb\\.|canary\\.)?discord\\.com/api/webhooks/').match(webhook_url):return _B
		async with aiohttp.ClientSession()as session:
			try:
				async with session.get(webhook_url)as response:await session.close();return _C if response.status==200 else _B
			except Exception:return _B
	async def delete(self,webhook_url=_D):
		'Delete a Discord webhook.\n\n        Args:\n            webhook_url (str, optional): Discord webhook URL to delete. Defaults to None.\n\n        Returns:\n            tuple: A tuple containing a boolean indicating success and an error message (if any).\n        ';webhook_url=webhook_url or self.webhook_url
		async with aiohttp.ClientSession()as session:
			try:
				async with session.delete(webhook_url)as response:await session.close()
				return _C,_D
			except Exception as e:return _B,e
	async def get(self,webhook_url=_D):
		'Retrieve information from a Discord webhook.\n\n        Args:\n            webhook_url (str, optional): Discord webhook URL to get information from. Defaults to None.\n\n        Returns:\n            dict: JSON data containing information from the webhook.\n        ';webhook_url=webhook_url or self.webhook_url
		async with aiohttp.ClientSession()as session:
			try:
				async with session.get(webhook_url)as response:await session.close();return await response.json()
			except Exception as e:return
	async def update(self,new_data,webhook_url=_D):
		'Update a Discord webhook with new data.\n\n        Args:\n            new_data (dict): New data to update the webhook.\n            webhook_url (str, optional): Discord webhook URL to update. Defaults to None.\n\n        Returns:\n            tuple: A tuple containing a boolean indicating success and an error message (if any).\n        ';webhook_url=webhook_url or self.webhook_url
		async with aiohttp.ClientSession()as session:
			try:
				async with session.patch(webhook_url,json=new_data)as response:await session.close()
				return _C,_D
			except Exception as e:return _B,e
message=_D
async def main():
	k='source_channel';j='username';h='Number of messages to send: ';g='saves\\embeds\\{}.json';f='Embed Description: ';d='Embed Title: ';c='saves\\plaintext\\{}.json';b='Is this the correct message? (y/n): ';Z='Would you like to load a saved message? (y/n): ';Y='Embeded Message';X='Regular Message';W='avatar';V='type';U='source_guild';T='s';S='Successfully sent message.';R='w';Q='Would you like to save this message for future use? (y/n): ';P='Message Content: ';O='Go Back';N='name';M='user';L='id';K='That option is not valid, Please try again.';J='Invalid Placeholder';I='Enter your option: ';H='saves\\plaintext';G='saves\\embeds';F='Press enter to continue...';E='content';D='\n';C='n';B='\n ';A='y';global message;util=Utilities();util.clear(util.log(_A,'Loading...',_B));util.title(f"UWT - Not logged in");os.makedirs('saves',exist_ok=_C);os.makedirs(G,exist_ok=_C);os.makedirs(H,exist_ok=_C);util.clear()
	while _C:
		util.title(f"UWT - Logging in...");webhook=WHT(input(util.log(_A,'Enter your webhook url: ',_B)))
		if webhook.webhook_url!='bypass':
			if not await webhook.validate():util.log(_E,'The webhook you provided is invalid.');continue
			else:data=await webhook.get();util.title(f"UWT - Logged in as {data[N]}")
		while _C:
			util.clear();menu,options=util.menu('Send Message','Spam Message','Delete Webhook','Webhook Information','Change Webhook Information','Logout');print(Center.Center(menu,50)+B*3)
			try:option=int(input(Center.XCenter(util.log(_A,I,_B),50)))
			except ValueError:option=J
			if option not in range(len(options)):util.clear();print(Center.Center(menu,50)+B*3);print(Center.XCenter(util.log(_E,K,_B),50));time.sleep(2.5)
			if option==1:
				while _C:
					util.clear();menu,options=util.menu(X,Y,O);print(Center.Center(menu,50)+B*3)
					try:option=int(input(Center.XCenter(util.log(_A,I,_B),50)))
					except ValueError:option=J
					if option not in range(len(options)):util.clear();print(Center.Center(menu,50)+B*3);print(Center.XCenter(util.log(_E,K,_B),50));time.sleep(2.5)
					if option in[1,2]:
						while _C:
							choice=input(Center.XCenter(util.log(_A,Z,_B),50)).lower()
							if choice==A:break
							elif choice==C:break
						util.clear()
						if choice==A:
							path=H if option==1 else G
							while _C:
								menu1,options1=util.menu(*os.listdir(path),O);util.clear();print(Center.Center(menu1,50)+B*3)
								try:option1=int(input(Center.XCenter(util.log(_A,I,_B),50)))-1
								except ValueError:option1=J
								if option1 not in range(len(options1)):util.clear();print(Center.Center(menu1,50)+B*3);print(Center.XCenter(util.log(_E,K,_B),50));time.sleep(2.5);continue
								with open(os.path.join(path,os.listdir(path)[option1]),'r+')as file:
									util.clear();message=json.load(file);ignored=[V]
									for a in message:
										if a in ignored:continue
										util.log(_A,f"{a}: {message[a]}")
									file.close();print(D)
								while _C:
									choice=input(util.log(_G,b,_B),50).lower()
									if choice==A:break
									elif choice==C:continue
					if option==1:
						if not message:
							content=input(util.log(_A,P,_B))
							while _C:
								choice=input(util.log(_A,Q,_B)).lower()
								if choice==A:
									file=c.format(len(os.listdir(H)))
									with open(file,R)as w:data={};data[E]=content;json.dump(data,w);w.close()
									break
								elif choice==C:break
						else:content=message[E]
						response,e=await webhook.send(content=content)
						if response:util.log(_F,S)
						else:util.log(_E,f"An error has occured: {e}.")
					elif option==2:
						if not message:
							embed=discord.Embed();embed.title=input(util.log(_A,d,_B));embed.description=input(util.log(_A,f,_B));content=input(util.log(_A,P,_B))
							while _C:
								choice=input(util.log(_A,Q,_B)).lower()
								if choice==A:
									file=g.format(len(os.listdir(G)))
									with open(file,R)as w:data=embed.to_dict();data[E]=content;json.dump(data,w);w.close()
									break
								elif choice==C:break
						else:embed=discord.Embed().from_dict(message);content=message[E]
						response,e=await webhook.send(embed=embed,content=content)
						if response:util.log(_F,S)
						else:util.log(_E,f"An error has occured: {e}.")
					elif option==0:break
					print(D);input(util.log(_A,F,_B))
			elif option==2:
				while _C:
					message=_D;util.clear();menu,options=util.menu(X,Y,O);print(Center.Center(menu,50)+B*3)
					try:option=int(input(Center.XCenter(util.log(_A,I,_B),50)))
					except ValueError:option=J
					if option not in range(len(options)):util.clear();print(Center.Center(menu,50)+B*3);print(Center.XCenter(util.log(_E,K,_B),50));time.sleep(2.5)
					if option in[1,2]:
						while _C:
							choice=input(Center.XCenter(util.log(_A,Z,_B),50)).lower()
							if choice==A:break
							elif choice==C:break
						util.clear()
						if choice==A:
							path=H if option==1 else G
							while _C:
								menu1,options1=util.menu(*os.listdir(path),O);util.clear();print(Center.Center(menu1,50)+B*3)
								try:option1=int(input(Center.XCenter(util.log(_A,I,_B),50)))-1
								except ValueError:option1=J
								if option1 not in range(len(options1)):util.clear();print(Center.Center(menu1,50)+B*3);print(Center.XCenter(util.log(_E,K,_B),50));time.sleep(2.5);continue
								with open(os.path.join(path,os.listdir(path)[option1]),'r+')as file:
									util.clear();message=json.load(file);ignored=[V]
									for a in message:
										if a in ignored:continue
										util.log(_A,f"{a}: {message[a]}")
									file.close();print(D)
								while _C:
									choice=input(util.log(_G,b,_B),50).lower()
									if choice==A:break
									elif choice==C:continue
					if option==1:
						while _C:
							try:iterations=int(input(util.log(_A,h,_B)));break
							except:pass
						if not message:
							content=input(util.log(_A,P,_B))
							while _C:
								choice=input(util.log(_A,Q,_B)).lower()
								if choice==A:
									file=c.format(len(os.listdir(H)))
									with open(file,R)as w:data={};data[E]=content;json.dump(data,w);w.close()
									break
								elif choice==C:break
						else:content=message[E]
						success=0
						for i in range(iterations):
							response,e=await webhook.send(content=content)
							if response:success+=1;util.log(_F,S)
							else:util.log(_E,f"An error has occured: {e}.")
						util.log(_A,f"Finished sending {iterations} messages. ({success} message{T if success>1 else _D} succeeded, {iterations-success} message{T if success>1 else _D} failed)");input(util.log(_A,F,_B));continue
					elif option==2:
						while _C:
							try:iterations=int(input(util.log(_A,h,_B)));break
							except:pass
						if not message:
							embed=discord.Embed();embed.title=input(util.log(_A,d,_B));embed.description=input(util.log(_A,f,_B));content=input(util.log(_A,P,_B))
							while _C:
								choice=input(util.log(_A,Q,_B)).lower()
								if choice==A:
									file=g.format(len(os.listdir(G)))
									with open(file,R)as w:data=embed.to_dict();data[E]=content;json.dump(data,w);w.close()
									break
								elif choice==C:break
						else:embed=discord.Embed().from_dict(message);content=message[E]
						success=0
						for i in range(iterations):
							response,e=await webhook.send(content=content,embed=embed)
							if response:success+=1;util.log(_F,S)
							else:util.log(_E,f"An error has occured: {e}.")
						util.log(_A,f"Finished sending {iterations} messages. ({success} message{T if success>1 else _D} succeeded, {iterations-success} message{T if success>1 else _D} failed)");input(util.log(_A,F,_B));continue
					elif option==0:break
			elif option==3:
				while _C:
					choice=input(util.log(_G,'Are you sure you want to delete this webhook? (y/n): ',_B)).lower()
					if choice==A:break
					elif choice==C:break
				if choice==A:
					response,e=await webhook.delete()
					if response:util.log(_F,'Successfully deleted webhook.')
					else:util.log(_E,f"An error has occured: {e}.")
					input(util.log(_A,F,_B))
				continue
			elif option==4:
				data=await webhook.get();print(D*3);wtype=data[V]
				if wtype==1:wtypestr='Incoming Webhook'
				elif wtype==2:wtypestr='Channel Follower Webhook'
				elif wtype==3:wtypestr='Application Webhook'
				else:wtypestr='Unknown Webhook Type'
				util.log(_A,f"General Webhook Information:");util.log(_A,f"Name: {data[N]}");util.log(_A,f"Type: {wtype} ({wtypestr})");util.log(_A,f"ID: {data[L]}");util.log(_A,f"Token: {data['token']}");util.log(_A,f"Avatar: {data[W]}");util.log(_A,f"Guild ID: {data['guild_id']}");util.log(_A,f"Channel ID: {data['channel_id']}");util.log(_A,f"Application ID: {data['application_id']}");util.log(_A,f"Avatar: {data[W]}")
				if wtype in[1,2]:print(D);util.log(_A,f"User Information:");util.log(_A,f"Username: {data[M][j]}");util.log(_A,f"Discriminator: {data[M]['discriminator']}");util.log(_A,f"ID: {data[M][L]}");util.log(_A,f"Avatar: {data[M][W]}");util.log(_A,f"Public Flags: {data[M]['public_flags']}")
				if wtype==2:print(D);util.log(_A,f"Source Information:");util.log(_A,f"Guild ID: {data[U][L]}");util.log(_A,f"Guild Name: {data[U][N]}");util.log(_A,f"Guild Icon: {data[U]['icon']}");util.log(_A,f"Guild ID: {data[U][L]}");util.log(_A,f"Channel ID: {data[k][L]}");util.log(_A,f"Channel Name: {data[k][N]}")
				print(D);input(util.log(_A,F,_B));continue
			elif option==5:
				username=input(util.log(_A,'Enter new username: ',_B))
				if username=='':util.log(_A,'No new username found, not proceeding...')
				else:
					response,e=await webhook.update({j:username})
					if response:util.log(_F,'Successfully updated webhook.')
					else:util.log(_E,f"An error has occured: {e}.")
				print(D);input(util.log(_A,F,_B))
			elif option==0:util.clear();break
if __name__=='__main__':asyncio.run(main())