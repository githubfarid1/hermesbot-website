from django.db import models

class Setting(models.Model):
    class Meta:
        ordering = ["id"]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)
    def __str__(self) -> str:
        return self.name

class Url(models.Model):
    class Meta:
        ordering = ["name"]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    mentionto = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self) -> str:
        return self.name

"""
Telegram Group/Channel ID
TELEGRAM_CHAT_ID
Telegram Bot Token
TELEGRAM_TOKEN
Proxy Helper
PROXY_HELPER
"""