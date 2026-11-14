from xbmc import executebuiltin


if __name__ == '__main__':
    executebuiltin(
        'RunScript(plugin.video.duskmate,open_sync_provider_settings,'
        'addon_id=script.module.duskmate.sync.tvdb)')
