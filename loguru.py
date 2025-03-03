#Loglama işlemleri yapmak
from loguru import logger

logger.debug("Bu bir DEBUG mesajıdır.")
logger.info("Bu bir İNFO mesajıdır.")
logger.success("İşlem başarıyla tamamlandı.")
logger.warning("Bu bir WARNİNG mesajıdır.")
logger.error("Bir hata meydana geldi.")
logger.critical("Kritik bir hata oluştu !")

logger.add("logfile.log", format="{time} {level} {message}", level="INFO")

logger.info("Bu mesaj log dosyasına yazılacak.")