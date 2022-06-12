from urllib.robotparser import RobotFileParser
import discord, asyncio, pytz, datetime
import os

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("이 문장은 Python의 내장 함수를 출력하는 터미널에서 실행됩니다\n지금 보이는 것 처럼 말이죠")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("봇의 상태매세지"))

@client.event
async def on_message(message):
    if message.content == "테스트": # 메세지 감지
        await message.channel.send ("{} | {}, Hello".format(message.author, message.author.mention))
        await message.author.send ("{} | {}, User, Hello".format(message.author, message.author.mention))

    if message.content.startswith ("!공지"):
        await message.delete()
        if message.author.guild_permissions.administrator:
            notice = message.content[4:]
            channel = client.get_channel(채널 ID)
            embed = discord.Embed(title="**공지사항 제목 (테스트)*", description="공지사항 내용은 항상 숙지 해주시기 바랍니다\n――――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――――".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. 조카크래파스-십팔색이야#0123 | 담당 관리자 : {}".format(message.author), icon_url="이미지 링크")
            embed.set_thumbnail(url="이미지 링크")
            await channel.send ("@everyone", embed=embed)
            await message.author.send("**[ BOT 자동 알림 ]** | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
 
        else:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

access_token = os.environ['BOT_TOKEN']
client.run(access_token)
