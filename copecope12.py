import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))

@client.event
async def on_message(message):
    if message.content.startswith('/eval'):
        try:
            cmd = message.content[6:]
            output = eval(cmd)
            await message.channel.send(output)
        except:
            await message.channel.send("오류가 발생했습니다.")

client.run("NzMxODcyNjkxODMzMDEyMzA0.Xw6Vxg.Ag8dlbl4BRf9OOfU17g1BnnT2ns")
