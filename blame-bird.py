#!/usr/bin/env python

""" This script tries to figure out the app responsible for
    a huge Library/Caches/com.apple.bird folder. """

import os
import uuid
import sqlite3
import os.path

def main():
    cache_path = os.path.expanduser('~/Library/Caches/com.apple.bird/session/g')
    unaccounted_for = set(map(uuid.UUID, os.listdir(cache_path)))
    client_db = sqlite3.connect(os.path.expanduser(
                '~/Library/Application Support/CloudDocs/session/db/client.db'))
    c = client_db.cursor()

    zones = {}
    zonesize = {}
    for rowid, name in c.execute('select rowid, zone_name from client_zones'):
        zones[rowid] = name
        zonesize[rowid] = 0

    for raw_guid, zone_id in c.execute(
            'select item_id, zone_rowid from client_unapplied_table'):
        # Apparently, not every item_id is an UUID.
        if len(raw_guid) != 16:
            continue
        guid = uuid.UUID(bytes=raw_guid)
        if guid not in unaccounted_for:
            continue
        path = os.path.join(cache_path, str(guid).upper())
        if not os.path.exists(path):
            continue
        zonesize[zone_id] += os.stat(path).st_size
        unaccounted_for.remove(guid)

    accounted_size = 0
    unaccounted_size = 0

    for zone_id, size in sorted(zonesize.items(), key=lambda x: x[1]):
        if size == 0:
            continue
        print '{:<45} {:>10.2f}MB'.format(zones[zone_id],
                        zonesize[zone_id] / 1000000.)
        accounted_size += zonesize[zone_id]

    for guid in unaccounted_for:
        path = os.path.join(cache_path, str(guid).upper())
        unaccounted_size += os.stat(path).st_size

    print
    print 'Accounted for: {}MB.  Still unaccounted: {}MB'.format(
                accounted_size / 1000000, unaccounted_size / 1000000)



if __name__ == '__main__':
    main()

