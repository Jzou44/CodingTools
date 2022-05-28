from flask import Blueprint
from Logic import Logic_MyIpAddress, Logic_UTIL, Logic_Config
from apscheduler.schedulers.background import BackgroundScheduler

logger = Logic_UTIL.get_logger(__name__)
Web_SideProject_blueprint = Blueprint('Web_SideProject_blueprint', __name__)

Logic_MyIpAddress.init_IP2Location_database()

if Logic_Config.FLAG_IS_PRODUCTION_ENV:
    # start side project

    schedule = BackgroundScheduler()
    # from Logic import Logic_Immigration
    #
    # schedule.add_job(func=Logic_Immigration.start_detect_news_change, trigger='interval',
    #                  seconds=Logic_Config.IMMIGRATION_NEWS_CHECK_INTERVAL_IN_SECONDS)

    from Logic import Logic_ImageUtilities

    schedule.add_job(func=Logic_ImageUtilities.clear_cache, trigger='interval',
                     minutes=Logic_Config.UPLOAD_TEMP_FOLDER_CLEAR_CACHE_INTERVAL_IN_MINUTES)
    schedule.start()
