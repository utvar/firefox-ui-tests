# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from marionette_driver import By

from firefox_puppeteer.ui_base_lib import UIBaseLib


class BaseDeck(UIBaseLib):

    def _create_panel_for_id(self, panel_id):
        """Creates an instance of :class:`Panel` for the specified panel id.

        :param panel_id: The ID of the panel to create an instance of.

        :returns: :class:`Panel` instance
        """
        mapping = {'apply': ApplyPanel,
                   'applyBillboard': ApplyBillboardPanel,
                   'checkForUpdates': CheckForUpdatesPanel,
                   'checkingForUpdates': CheckingForUpdatesPanel,
                   'downloadAndInstall': DownloadAndInstallPanel,
                   'downloadFailed': DownloadFailedPanel,
                   'downloading': DownloadingPanel,
                   'feedPanel': FeedPanel,
                   'generalPanel': GeneralPanel,
                   'mediaPanel': MediaPanel,
                   'noUpdatesFound': NoUpdatesFoundPanel,
                   'permPanel': PermissionsPanel,
                   'securityPanel': SecurityPanel
                   }

        panel = self.element.find_element(By.ID, panel_id)
        return mapping.get(panel_id, BasePanel)(lambda: self.marionette, self.window, panel)


class BasePanel(UIBaseLib):

    def __eq__(self, other):
        return self.element.get_attribute('id') == other.element.get_attribute('id')

    def __ne__(self, other):
        return self.element.get_attribute('id') != other.element.get_attribute('id')

    def __str__(self):
        return self.element.get_attribute('id')
