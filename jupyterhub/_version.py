"""JupyterHub version info"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

version_info = (
    0,
    8,
    0,
    'dev',
)

__version__ = '.'.join(map(str, version_info))


def _check_version(hub_version, singleuser_version, log):
    """Compare Hub and single-user server versions"""
    if not hub_version:
        log.warning("Hub has no version header, which means it is likely < 0.8. Expected %s", __version__)
        return

    if not singleuser_version:
        log.warning("Single-user server has no version header, which means it is likely < 0.8. Expected %s", __version__)
        return

    # compare minor X.Y versions
    if hub_version != singleuser_version:
        from distutils.version import LooseVersion as V
        hub_major_minor = V(hub_version).version[:2]
        singleuser_major_minor = V(singleuser_version).version[:2]
        if singleuser_major_minor == hub_major_minor:
            # patch-level mismatch or lower, log difference at debug-level
            # because this should be fine
            log_method = log.debug
        else:
            # log warning-level for more significant mismatch, such as 0.8 vs 0.9, etc.
            log_method = log.warning
        log_method("jupyterhub version %s != jupyterhub-singleuser version %s",
            hub_version, singleuser_version,
        )
    else:
        log.debug("jupyterhub and jupyterhub-singleuser both on version %s" % hub_version)