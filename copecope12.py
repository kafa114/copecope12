import discord
import asyncio

client = discord.Client()

if message.content.startswith('/eval'):
    try:
        cmd = message.content[6:]
        output = eval(cmd)
        await message.channel.send(output)
    except:
        await message.channel.send("오류가 발생했습니다.")

client.run("NzMxODcyNjkxODMzMDEyMzA0.Xw6Vxg.Ag8dlbl4BRf9OOfU17g1BnnT2ns")
