Changelog for Onadata
=====================

``* represents releases that introduce new migrations``

v2.5.10(2021-11-01)
-------------------

- Bump the `ona-oidc` requirement to v0.0.8.
  `PR #2162 <https://github.com/onaio/onadata/pull/2162>`_
  [@DavisRayM]
- Return X-OpenRosa-Accept-Content-Length header for requests failing with 401 status code.
  `PR #2152 <https://github.com/onaio/onadata/pull/2152>`_
  [@WinnyTroy]

v2.5.10(2021-10-7)
------------------

- Ensure that `user_profile` is serialized before caching
  `PR #2147 <https://github.com/onaio/onadata/pull/2147>`_
  [@FrankApiyo]
- Clean out related object upon XForm deletion
  `PR 2136 <https://github.com/onaio/onadata/pull/2136>`_
  [@WinnyTroy]
- Allow users to filter by NULL on the data endpoint
  `PR #2144 <https://github.com/onaio/onadata/pull/2144>`_
  [@WinnyTroy]
- Add management command to remove columns from submission XML
  `PR #2143 <https://github.com/onaio/onadata/pull/2143>`_
  [@DavisRayM]
- Bump ona-oidc version from v0.0.6 to v0.0.7
  `PR #2154 <https://github.com/onaio/onadata/pull/2154>`_
  [@DavisRayM]
- Generate XForm headers in CSV exports for XForms without submissions
  `PR #2137 <https://github.com/onaio/onadata/pull/2137>`_
  [@WinnyTroy]
- Query optimizations for the Briefcase viewset
  `PR #2142 <https://github.com/onaio/onadata/pull/2142>`_
  [@DavisRayM]

v2.5.9(2021-08-27)
------------------

- Ensure exports are re-generated on submission delete
  `PR #2132 <https://github.com/onaio/onadata/pull/2132>`_
  [@DavisRayM]
- Update validation checks that are run on XForm titles
  `PR #2135 <https://github.com/onaio/onadata/pull/2135>`_
  [@WinnyTroy]
- Ensure Pagination and sorting are implemented on the data endpoint
  `PR #2113 <https://github.com/onaio/onadata/pull/2113>`_
  [@WinnyTroy]
- Ensure internal routing is supported on the onadata-uwsgi docker image
  `PR #2134 <https://github.com/onaio/onadata/pull/2134>`_
  [@DavisRayM]
- Remove namespace attribute from returned XML if present
  `PR #2139 <https://github.com/onaio/onadata/pull/2139>`_
  [@DavisRayM]
- Ensure incomplete submissions are not returned on the Briefcase API
  `PR #2140 <https://github.com/onaio/onadata/pull/2140>`_
  [@DavisRayM]

v2.5.8(2021-07-29)
------------------

- Add retrieve_org_or_project_list management command
  `PR #2098 <https://github.com/onaio/onadata/pull/2098>`_
  [@DavisRayM]
- Open ID - Add name claim splitting functionality
  `PR #2109 <https://github.com/onaio/onadata/pull/2109>`_
  [@DavisRayM]
- Add metadata fields present in the JSON response to the XML response
  `PR #2114 <https://github.com/onaio/onadata/pull/2114>`_
  [@DavisRayM]
- Replace internal OpenID Connect tools for `ona-oidc <https://github.com/onaio/ona-oidc>`_
  `PR #2096 <https://github.com/onaio/onadata/pull/2096>`_
  [@WinnyTroy]
- Ensure content-disposition header is correctly encoded
  `PR #2116 <https://github.com/onaio/onadata/pull/2116>`_
  [@DavisRayM]
- Add enketo encryption namespaces
  `PR #2122 <https://github.com/onaio/onadata/pull/2122>`_
  [@denniswambua]
- Add sumission review docs to main index file
  `PR #2123 <https://github.com/onaio/onadata/pull/2123>`_
  [@WinnyTroy]
- Withdraw user email from user activity metric data
  `PR #2124 <https://github.com/onaio/onadata/pull/2124>`_
  [@WinnyTroy]
- Add signals that send out emails for accounts that are in-active
  `PR #2127 <https://github.com/onaio/onadata/pull/2127>`_
  [@DavisRayM]

v2.5.7(2021-06-14)
------------------

- Update data endpoint documentation
  `PR #2100 <https://github.com/onaio/onadata/pull/2100>`_
  [@WinnyTroy]
- Add service_health view function
  `PR #2097 <https://github.com/onaio/onadata/pull/2097>`_
  [@DavisRayM]
- Add CI Test Github Actions workflow
  `PR #2102 <https://github.com/onaio/onadata/pull/2102>`_
  [@DavisRayM]

v2.5.6(2021-06-02)
------------------

- Expose ability to delete a subset or all submissions from the data endpoint
  `PR #2076 <https://github.com/onaio/onadata/pull/2076>`_
  [@WinnyTroy]
- Tableau WDC media file urls enhancement
  `PR #2074 <https://github.com/onaio/onadata/pull/2074>`_
  [@WinnyTroy]
- Add the default authentication classes to the export viewset
  `PR #2023 <https://github.com/onaio/onadata/pull/2023>`_
  [@DavisRayM]
- Update requirements
  `PR #2070 <https://github.com/onaio/onadata/pull/2070>`_
  [@DavisRayM]
- Check if user is an AnonymousUser before trying to retrieve their project role
  `PR #2084 <https://github.com/onaio/onadata/pull/2084>`_
  [@DavisRayM]
- Add optional `flow_title` field to the TextItService
  `PR #2086 <https://github.com/onaio/onadata/pull/2086>`_
  [@DavisRayM]
- Update onadata-uwsgi docker file
  `PR #2087 <https://github.com/onaio/onadata/pull/2087>`_
  [@DavisRayM]
- Expound on field query param for the data json format and geojson format
  `PR #2085 <https://github.com/onaio/onadata/pull/2085>`_
  [@WinnyTroy]
- Add `error_message` field to the Export serializer
  `PR #2094 <https://github.com/onaio/onadata/pull/2094>`_
  [@DavisRayM]

v2.5.5(2021-05-17)
------------------

- Add documentation for the messaging endpoint 
  `PR #2026 <https://github.com/onaio/onadata/pull/2026>`_
  [@DavisRayM]
- Fix submission deletion endpoint error
  `PR #2060 <https://github.com/onaio/onadata/pull/2060>`_
  [@DavisRayM]
- Add review date column on data exports
  `PR #2057 <https://github.com/onaio/onadata/pull/2057>`_
  [@DavisRayM]
- Ignore accepted renderer & media type for the export async endpoint
  `PR #2027 <https://github.com/onaio/onadata/pull/2027>`_
  [@denniswambua]
- Project - XForm shared status sync changes
  `PR #2049 <https://github.com/onaio/onadata/pull/2049>`_
  [@DavisRayM]
- Ensure project owners are able to view all their collaborators from the project list
  `PR #2073 <https://github.com/onaio/onadata/pull/2073>`_
  [@DavisRayM]
- Add pagination for the messaging endpoint
  `PR #2068 <https://github.com/onaio/onadata/pull/2068>`_
  [@DavisRayM]
- Remove #text element from XML responses
  `PR #2079 <https://github.com/onaio/onadata/pull/2079>`_
  [@DavisRayM]
- Track users who initiate CSV imports
  `PR #2078 <https://github.com/onaio/onadata/pull/2078>`_
  [@DavisRayM]
- Set status to imported_via_csv for CSV Imported submissions
  `PR #2077 <https://github.com/onaio/onadata/pull/2077>`_
  [@DavisRayM]

v2.5.4(2021-04-23)
------------------

- Add review date
  `PR #2044 <https://github.com/onaio/onadata/pull/2044>`_
  [@WinnyTroy]
- Add support for sort and handle streaming of empty datasets on XML Responses
  `PR #2039 <https://github.com/onaio/onadata/pull/2039>`_
  [@DavisRayM]
- Ensure that the CSV Import status is updated on failed import
  `PR #2046 <https://github.com/onaio/onadata/pull/2046>`_
  [@DavisRayM]
- Update Django version to the latest 2.2.* version
  `PR #2047 <https://github.com/onaio/onadata/pull/2047>`_
  [@DavisRayM]

v2.5.3(2021-03-23)
------------------

- Add github workflow to build an AWS ECR image
  `PR #2034 <https://github.com/onaio/onadata/pull/2034>`_
  [@DavisRayM]
- Publish arm64 Docker Image
  `PR #2042 <https://github.com/onaio/onadata/pull/2042>`_
  [@morrismukiri]
- Lockout IP Changes
  `PR #2040 <https://github.com/onaio/onadata/pull/2040>`_
  [@DavisRayM]

v2.5.2(2021-03-10)
------------------

- Fix "Different root node name" issue
  `PR #2029 <https://github.com/onaio/onadata/pull/2029>`_
  [@DavisRayM]
- Update PyXForm dependency to v1.4.0
  `PR #2031 <https://github.com/onaio/onadata/pull/2031>`_
  [@DavisRayM]

v2.5.1(2021-02-23)
------------------

- Use master database when updating an XForms Submission Count
  `PR #2002 <https://github.com/onaio/onadata/pull/2002>`_
  [@DavisRayM]
- Lockout users based on specific IPs instead of username
  `PR #1978 <https://github.com/onaio/onadata/pull/1978>`_
  [@DavisRayM]
- Add pagination & xml support to the data list endpoint
  `PR #2005 <https://github.com/onaio/onadata/pull/2005>`_
  [@DavisRayM]
- Paginate data list responses after a configurable threshold
  `PR #2010 <https://github.com/onaio/onadata/pull/2010>`_
  [@DavisRayM]
- Trigger error on url in xform title
  `PR #2007 <https://github.com/onaio/onadata/pull/2007>`_
  [@ivermac]
- Check if XForm is a MergedXForm and merge field choices if it is(a MergedXForm)
  `PR #2011 <https://github.com/onaio/onadata/pull/2011>`_
  [@FrankApiyo]
- Support query by date_modified field *
  `PR #2009 <https://github.com/onaio/onadata/pull/2009>`_
  [@DavisRayM]
- Capture attachment file names whose name exceeds 100 chars
  `PR #2003 <https://github.com/onaio/onadata/pull/2003>`_
  [@WinnyTroy]
- Merge select one and select multiple options at MergedXform creation
  `PR #2015 <https://github.com/onaio/onadata/pull/2015>`_
  [@FrankApiyo]
- Use language parameter to create exports
  `PR #2014 <https://github.com/onaio/onadata/pull/2014>`_
  [@FrankApiyo]
- Fix Charts endpoint JSON response not rendering
  `PR #2022 <https://github.com/onaio/onadata/pull/2022>`_
  [@DavisRayM]

v2.5.0(2021-01-21)
------------------

- Clear cache and refresh user profile on email verification
  `PR #1970 <https://github.com/onaio/onadata/pull/1970>`_
  [@DavisRayM]
- Add timestamp filter for the Messaging Viewset
  `PR #1973 <https://github.com/onaio/onadata/pull/1973>`_
  [@DavisRayM]
- Introduce Tableau v2
  `PR #1910 <https://github.com/onaio/onadata/pull/1910>`_
  [@WinnyTroy]
- Handle TypeError raised when `current_count` value is None
  `PR #1980 <https://github.com/onaio/onadata/pull/1980>`_
  [@DavisRayM]
- Add pagination headers to the paginated DataViewSet response
  `PR #1977 <https://github.com/onaio/onadata/pull/1977>`_
  [@DavisRayM]
- Add support for querying a column with multiple conditions
  `PR #1981 <https://github.com/onaio/onadata/pull/1981>`_
  [@DavisRayM]
- Retrieve user profile using case insensitive username filter
  `PR #1988 <https://github.com/onaio/onadata/pull/1988>`_
  [@DavisRayM]
- validate input fields on put form endpoint requests
  `PR #1991 <https://github.com/onaio/onadata/pull/1991>`_
  [@ivermac]
- Update Tableau Documentation
  `PR #1989 <https://github.com/onaio/onadata/pull/1989>`_
  [@WinnyTroy]
- sanitize input recieved by media endpoint
  `PR #1997 <https://github.com/onaio/onadata/pull/1997>`_
  [@ivermac]

v2.4.9(2020-12-17)
------------------

- Update submission metrics collection
  `PR #1895 <https://github.com/onaio/onadata/pull/1895>`_
  [@WinnyTroy]
- XForm and Data ViewSet updates
  `PR #1971 <https://github.com/onaio/onadata/pull/1971>`_
  [@DavisRayM]

v2.4.8(2020-12-14)
------------------

- Fix failing URL upload test
  `PR #1954 <https://github.com/onaio/onadata/pull/1954>`_
  [@DavisRayM]
- Add enketo-preview url routed to PreviewXFormListViewSet
  `PR #1953 <https://github.com/onaio/onadata/pull/1953>`_
  [@FrankApiyo]
- Data viewset retrieval optimisations
  `PR #1966 <https://github.com/onaio/onadata/pull/1966>`_
  [@DavisRayM]
- Update "onadata-uwsgi" docker file
  `PR #1956 <https://github.com/onaio/onadata/pull/1956>`_
  [@DavisRayM]

v2.4.7(2020-11-16)
------------------

- Change Instance Webhooks to be fully asynchronous
  `PR #1949 <https://github.com/onaio/onadata/pull/1949>`_
  [@DavisRayM]

2.4.6(2020-11-10)
-----------------

- Ensure project permissions are upgraded on project transfer
  `PR #1932 <https://github.com/onaio/onadata/pull/1905>`_
  [@DavisRayM]
- Check submission encryption status before Instance creation
  `PR #1938 <https://github.com/onaio/onadata/pull/1938>`_
  [@DavisRayM]
- Downgrade celery requirement
  `PR #1942 <https://github.com/onaio/onadata/pull/1942>`_
  [@DavisRayM]
- Dockerfile updates
  `PR #1937 <https://github.com/onaio/onadata/pull/1937>`_
  [@DavisRayM]

v2.4.5(2020-10-23)
------------------

- Update Requirements
  `PR #1905 <https://github.com/onaio/onadata/pull/1905>`_
  [@DavisRayM]

v2.4.4(2020-10-15)
------------------

- Re-set project cache using up-to-date project object
  `PR #1927 <https://github.com/onaio/onadata/pull/1927>`_
  [@DavisRayM]

v2.4.3(2020-10-12)
------------------

- Project Viewset: Caching refactor
  `PR #1902 <https://github.com/onaio/onadata/pull/1902>`_
  [@DavisRayM]
- Ensure only select_multiple questions are flattened into one column
  `PR #1912 <https://github.com/onaio/onadata/pull/1912>`_
  [@DavisRayM]
- Handle replication lag when authenticating with a Bearer Token
  `PR #1922 <https://github.com/onaio/onadata/pull/1922>`_
  [@DavisRayM]

v2.4.2(2020-09-21)
------------------

- CSV Import: Handle re-importing of select_multiple questions
  `PR #1852 <https://github.com/onaio/onadata/pull/1852>`_
  [@DavisRayM]
- Limit message payload sizes
  `PR #1893 <https://github.com/onaio/onadata/pull/1893>`_
  [@DavisRayM]
- Main API view updates
  `PR #1900 <https://github.com/onaio/onadata/pull/1900>`_
  [@DavisRayM]

v2.4.1(2020-09-03)
------------------

- Fix enketo edit link generation
  `PR #1887 <https://github.com/onaio/onadata/pull/1887>`_
  [@DavisRayM]

v2.4.0(2020-09-01)
------------------

- Initial support for tracking submissions with Segment
  `PR #1872 <https://github.com/onaio/onadata/pull/1872>`_
  [@DavisRayM]
- Add caching to the organization profile viewset
  `PR #1876 <https://github.com/onaio/onadata/pull/1876>`_
  [@FrankApiyo]
- Include support for repeat groups in the Tableau-Onadata integration
  `PR #1845 <https://github.com/onaio/onadata/pull/1845>`_
  [@WinnyTroy]
- Enketo intergration updates
  `PR #1857 <https://github.com/onaio/onadata/pull/1845>`_
  [@WinnyTroy]
- Unpack GPS data into separate columns for altitude, precision, latitude and longitude
  `PR #1880 <https://github.com/onaio/onadata/pull/1880>`_
  [@WinnyTroy]

v2.3.8(2020-08-25)
------------------

- Fix an issue where project endpoint cache would stay stale on Project Update
  `PR #1874 <https://github.com/onaio/onadata/pull/1847>`_
  [@FrankApiyo]
- Add support for email:password login on the main views
  `PR #1878 <https://github.com/onaio/onadata/pull/1878>`_
  [@DavisRayM]

v2.3.7(2020-08-11)
------------------

- Add a way to elongate `ODKToken` expiry data *
  `PR #1847 <https://github.com/onaio/onadata/pull/1847>`_
  [@DavisRayM]
- Set the correct root node for created submissions
  `PR #1853 <https://github.com/onaio/onadata/pull/1853>`_
  [@DavisRayM]
- Ensure only XForm admins & managers can review submissions
  `PR #1864 <https://github.com/onaio/onadata/pull/1864>`_
  [@DavisRayM]
- Stop duplication of RapidPro submissions on edit
  `PR #1869 <https://github.com/onaio/onadata/pull/1869>`_
  [@DavisRayM]

v2.3.6(2020-07-29)
------------------

- Return FLOIP data for Merged Datasets*
  `PR #1773 <https://github.com/onaio/onadata/pull/1773>`_
  [@DavisRayM]
- Add deletion suffix to a Users email upon soft deletion
  `PR #1844 <https://github.com/onaio/onadata/pull/1844>`_
  [@WinnyTroy]
- Add more flexible MQTT Topics
  `PR #1850 <https://github.com/onaio/onadata/pull/1850>`_
  [@lincmba]
- Include support for `select_multiple` questions on Tableau connector
  `PR #1835 <https://github.com/onaio/onadata/pull/1850>`_
  [@WinnyTroy]

v2.3.5(2020-06-18)
------------------

- Introduced caching for UserProfile objects
  `PR #1823 <https://github.com/onaio/onadata/pull/1823>`_
  [@WinnyTroy]
- Send CRUD notifications for Forms, Submissions and SubmissionReviews
  `PR #1793 <https://github.com/onaio/onadata/pull/1793>`_
  [@lincmba]
- Set enketo cookie `__enketo_meta_username` on login
  `PR #1834 <https://github.com/onaio/onadata/pull/1834>`_
  [@FrankApiyo]

v2.3.4(2020-06-15)
------------------

- Use last name as first name if not present in OpenID Connect identification token
  `PR #1831 <https://github.com/onaio/onadata/pull/1831>`_
  [@DavisRayM]

v2.3.3(2020-05-19)
------------------

- Fix an issue where file attachments/uploads were automatically soft-deleted
  `PR #1816 <https://github.com/onaio/onadata/pull/1816>`_
  [@DavisRayM]
- Cache projects after creation and retrieve the project from cache in subsequent requests
  `PR #1819 <https://github.com/onaio/onadata/pull/1819>`_
  [@KipSigei]
- Fix an issue where anonymous submissions from Enketo would fail
  `PR #1825 <https://github.com/onaio/onadata/pull/1825>`_
  [@WinnyTroy]
- Add a management command that deletes users
  `PR #1717 <https://github.com/onaio/onadata/pull/1717>`_
  [@WinnyTroy]
- Ensure that authenticated users can only submit to forms they have access to
  `PR #1804 <https://https://github.com/onaio/onadata/pull/1804>`_
  [@DavisRayM]
- Add support for Tableau v2
  `PR #1820 <https://github.com/onaio/onadata/pull/1820>`_
  [@WinnyTroy]
- Add setting to optional turn off creation of public projects & xforms
  `PR #1829 <https://github.com/onaio/onadata/pull/1829>`_
  [@DavisRayM]

v2.3.2(2020-05-05)
------------------

- Update google sheets connection when data is updated or deleted
  `PR #1808 <https://github.com/onaio/onadata/pull/1808>`_
  [@KipSigei]
- Fix errors encountered when utilizing a master-replica database setup
  `PR #1813 <https://github.com/onaio/onadata/pull/1813>`_
  [@DavisRayM]

v2.3.1(2020-04-14)
------------------

- Use master database when fetching external export metadata information
  `PR #1760 <https://github.com/onaio/onadata/pull/1760>`_
  [@WinnyTroy]
- Add support for latest RapidPro webhook posts
  `PR #1807 <https://github.com/onaio/onadata/pull/1807>`_
  [@DavisRayM]
- Handle dynamic choice names while generating SAV exports
  `PR #1806 <https://github.com/onaio/onadata/pull/1806>`_
  [@DavisRayM]

v2.3.0(2020-04-07)*
-------------------

- Set deletied_by field when deleting XForms asynchronously
  `PR #1798 <https://github.com/onaio/onadata/pull/1798>`_
  [@DavisRayM]
- Add and utilize consistent enketo URLS
  `PR #1775 <https://github.com/onaio/onadata/pull/1775>`_
  `PR #1799 <https://github.com/onaio/onadata/pull/1775>`_
  [@DavisRayM]
- Invalidate sessions on password change
  `PR #1783 <https://github.com/onaio/onadata/pull/1783>`_
  [@DavisRayM]
- Update dependencies
  `PR #1788 <https://github.com/onaio/onadata/pull/1788>`_
  [@DavisRayM]
- Update PyXForm to v1.1.0
  `PR #1796 <https://github.com/onaio/onadata/pull/1796>`_
  [@DavisRayM]

v2.2.1 (2020-02-20)*
-------------------

Bug fixes and changes
#####################
- Upgrade pyxform to v0.15.1
  `PR #1722 <https://github.com/onaio/onadata/pull/1722>`_
  [@DavisRayM]

- Add ability to soft-delete attachments
  `PR #1698 <https://github.com/onaio/onadata/pull/1698>`_
  [@WinnyTroy]

- Update requirement files
  `PR #1785 <https://github.com/onaio/onadata/pull/1785>`_
  [@DavisRayM]

v2.2.0 (2020-02-12)*
___________________

Bug fixes and changes
#####################
- Set X-Frame-Options-Middleware
  `PR #1766 <https://github.com/onaio/onadata/pull/1766>`_
  [@WinnyTroy]

- Handle error thrown by urllib
  `PR #1765 <https://github.com/onaio/onadata/pull/1765>`_
  [@DavisRayM]

- Allow the $or filter to accept null values
  `PR #1749 <https://github.com/onaio/onadata/pull/1749>`_
  [@DavisRayM]

- Upgrade to Django v2.2
  `PR #1770 <https://github.com/onaio/onadata/pull/1770>`_
  [@DavisRayM]

v2.1.2 (2020-01-09)
___________________

Bug fixes and changes
#####################

- Enforce case-insensitivity for the username when making a submission
  `PR #1762 <https://github.com/onaio/onadata/pull/1762>`_
  [@DavisRayM]

- Fix an issue caused by Owners of organizations lacking permissions to the Organization User Profile
  `PR #1757 <https://github.com/onaio/onadata/pull/1757>`_
  [@DavisRayM]

- Enforce datatype constraints on CSV Imports
  `PR #1716 <https://github.com/onaio/onadata/pull/1716>`_
  [@DavisRayM]

v2.1.1 (2020-01-08)*
___________________

Bug fixes and changes
#####################

- Add contribution guideline, issue template and pull request template
  `PR #1750 <https://github.com/onaio/onadata/pull/1750>`_
  [@DavisRayM]

- Properly handle spaces within CSV usernames while sharing project
  `PR #1741 <https://github.com/onaio/onadata/pull/1741>`_
  [@DavisRayM]

- Allow null values on the database level for the public_key field in the XForm model
  `PR #1740 <https://github.com/onaio/onadata/pull/1740>`_
  [@DavisRayM]

- Fix issue where the /orgs endpoint would return duplicate member names
  `PR #1752 <https://github.com/onaio/onadata/pull/1752>`_
  [@ukanga]

- Allow any user to submit to a form when require_authentication is False
  `PR #1753 <https://github.com/onaio/onadata/pull/1753>`_
  [@FrankApiyo]

- Only return projects tied to an Active user
  `PR #1732 <https://github.com/onaio/onadata/pull/1732>`_
  [@FrankApiyo]

v2.1.0 (2019-12-06)*
-------------------

New Features
############

- Add ODKToken model and authentication
  `PR #1705 <https://github.com/onaio/onadata/pull/1705>`_
  `PR #1707 <https://github.com/onaio/onadata/pull/1707>`_
  `PR #1712 <https://github.com/onaio/onadata/pull/1712>`_
  [@DavisRayM]

- Add ability to share a project to multiple users
  `PR #1704 <https://github.com/onaio/onadata/pull/1704>`_
  [@DavisRayM]

- Add OpenID Connect functionality
  `PR #1706 <https://github.com/onaio/onadata/pull/1706>`_
  `PR #1727 <https://github.com/onaio/onadata/pull/1727>`_
  [@ivermac , @DavisRayM]

- Add ability to encrypt forms after creation
  `PR #1708 <https://github.com/onaio/onadata/pull/1708>`_
  [@DavisRayM]

- Add a way to deactivate organizations by default on create
  `PR #1733 <https://github.com/onaio/onadata/pull/1733>`_
  [@DavisRayM]

Bug fixes and changes
#####################

- Fix form level permission restrictions on search
  `PR #1691 <https://github.com/onaio/onadata/pull/1691>`_
  [@lincmba]

- Validate auth user username before creating Registration Profile
  `PR #1680 <https://github.com/onaio/onadata/pull/1680>`_
  [@WinnyTroy]

- Modify flow results response endpoints response formatting
  `PR #1695 <https://github.com/onaio/onadata/pull/1695>`_
  [@DavisRayM]

- Use the master database when calling notification backends
  `PR #1703 <https://github.com/onaio/onadata/pull/1703>`_
  [@DavisRayM]

- Fix MemCachedLengthError when locking out users
  `PR #1713 <https://github.com/onaio/onadata/pull/1713>`_
  [@DavisRayM]

- Return non digit XForm versions
  `PR #1728 <https://github.com/onaio/onadata/pull/1728>`_
  [@DavisRayM]

- Stop lower casing usernames when retrieving users through XFormListViewSet
  `PR #1738 <https://github.com/onaio/onadata/pull/1738>`_
  [@DavisRayM]

- Return members of the Owner team on the /orgs endpoint
  `PR #1734 <https://github.com/onaio/onadata/pull/1734>`_
  [@DavisRayM]

2.0.11 (2019-09-19)
-------------------
- Send email only once in a lockout session
  `Issue #1687 <https://github.com/onaio/onadata/pull/1687>`_
  [@ukanga]

- Ignore ODK APIs on lockout session checks
  `Issue #1688 <https://github.com/onaio/onadata/pull/1688>`_
  [@ukanga]

2.0.10 (2019-09-04)
-------------------
- Include create model mixin to the Connect Viewset
  `PR #1683 <https://github.com/onaio/onadata/pull/1683>`_
  [@WinnyTroy]


2.0.9 (2019-09-03)
--------------------
- Submission Review fails when payload is used
  `PR #1623 <https://github.com/onaio/onadata/issues/1623>`_
  [@lincmba, @WinnyTroy]

- Only use type, name and label columns when merging forms
  `PR #1587 <https://github.com/onaio/onadata/issues/1587>`_
  [@WinnyTroy]


2.0.8 (2019-08-21)
-------------------
- Include media-type filter on media endpoint
  `PR #1644 <https://github.com/onaio/onadata/issues/1644>`_
  [@WinnyTroy]

- Create count endpoint to get total number of attachments in media enpoint
  `PR #1665 <https://github.com/onaio/onadata/pull/1665>`_
  [@RayceeM]

- Set rate limits on change password attempts
  `PR #1675 <https://github.com/onaio/onadata/issues/1675>`_
  [@RayceeM]

- Override django inbuilt password reset token generation
  `PR #1651 <https://github.com/onaio/onadata/issues/1651>`_
  [@WinnyTroy]

- Switch email headers attributes for user verification emails
  `PR #1667 <https://github.com/onaio/onadata/issues/1667>`_
  [@WinnyTroy]


2.0.7 (2019-07-24)
-------------------
- Fix maximum recursion depth error on caching login attempts
  `PR #1661 <https://github.com/onaio/onadata/issues/1661>`_
  [@ukanga]


2.0.6 (2019-07-17)
-------------------
- Handle negative number strings to number values correctly
  `PR #1641 <https://github.com/onaio/onadata/issues/1641>`_
  [@WinnyTroy]

- Fix MemcachedKeyCharacterError error
  `PR #1653 <https://github.com/onaio/onadata/issues/1653>`_
  [@ukanga]


2.0.5 (2019-07-15)
-------------------
- Replace load_class with Django's import_string function
  `PR #1636 <https://github.com/onaio/onadata/issues/1636>`_
  [@p-netm]

- Set deleted_by user on submission deletions.
  `PR #1640 <https://github.com/onaio/onadata/issues/1640>`_
  [@WinnyTroy]

- Handle OperationalError exceptions due to canceling statement due to conflicts
  `PR #906 <https://github.com/onaio/onadata/issues/906>`_
  [@WinnyTroy]

- Prevent KeyError exceptions on missing labels for SPSS exports
  `PR #1629 <https://github.com/onaio/onadata/issues/1629>`_
  [@WinnyTroy]

- Add attachment type filter on attachments endpoint
  `PR #1644 <https://github.com/onaio/onadata/issues/1644>`_
  [@WinnyTroy]


2.0.4 (2019-06-13)
-------------------
- Only convert to string sav_writer values.
  `PR #1621 <https://github.com/onaio/onadata/pull/1621>`_
  [@lincmba]

- Rate-Limit login attempts
  `PR #1622 <https://github.com/onaio/onadata/pull/1622>`_
  [@lincmba]

- Allow blank notes in reviewing Approved/Pending submissions
  `Fixes #1623 <https://github.com/onaio/onadata/issues/1623>`_
  [@lincmba]

- Fix TypeError on getting async csv import status
  `Fixes #1624 <https://github.com/onaio/onadata/issues/1624>`_
  [@lincmba]


2.0.3 (2019-06-06)
-------------------
- Get rid of _async keyword on Parsed Instance save() method
  `Fixes #1615 <https://github.com/onaio/onadata/pull/1618>`_
  [@lincmba]

- Pin temptoken authentication to master database
  `Fixes #1616 <https://github.com/onaio/onadata/pull/1617>`_
  [@lincmba]


2.0.2 (2019-05-30)
-------------------
- Rename variables whose name is async
  `Fixes #1608 <https://github.com/onaio/onadata/issues/1606>`_
  [@ivermac ]

- Process uid as string not binary
  `Fixes #1610 <https://github.com/onaio/onadata/issues/1610>`_
  [@lincmba ]



2.0.1 (2019-05-28)
-------------------
- Remove message attribute from Exceptions
  `Fixes #1609 <https://github.com/onaio/onadata/issues/1609>`_
  [@lincmba]


2.0.0 (2019-05-24)
-------------------
- Handle errors in custom renderers.
  `Fixes #1598 <https://github.com/onaio/onadata/issues/1598>`_
  [@lincmba]

- Check report_xform permission on enketo URL requests
  `PR #1602 <https://github.com/onaio/onadata/pull/1602>`_
  [@ukanga]

- Upgrade to django 2.0
  `PR #1559 <https://github.com/onaio/onadata/pull/1559>`_
  [@bmarika, @lincmba]

1.19.4 (2019-04-08)
-------------------
- Expose submissions URL to Enketo.
  `Pull #1526 <https://github.com/onaio/onadata/pull/1526>`_
  [@WinnyTroy and @lincmba]

- Load one image at a time in classic photo view.
  `Fix #1560 <https://github.com/onaio/onadata/issues/1560>`_
  [@lincmba]

- Add transferproject command to transfer project between users.
  `Issue #1491 <https://github.com/onaio/onadata/issues/1491>`_
  [@bmarika]

- Add MetaData.submission_review() function for submission reviews metadata.
  `Fix #1585 <https://github.com/onaio/onadata/issues/1585>`_
  [@lincmba]

- Fixes on ZIP_REPORT_ATTACHMENT_LIMIT
  `Fix #1592 <https://github.com/onaio/onadata/issues/1592>`_
  [@lincmba]

- Fix unicode TypeError on publishing text_xls_form strings.
  `Fix #1593 <https://github.com/onaio/onadata/issues/1593>`_
  [@ukanga]


1.19.3 (2019-03-08)
-----------------------
- Convert excel date format to csv format
  `Fixes #1577 <https://github.com/onaio/onadata/issues/1577>`_
  [@lincmba]

1.19.2 (2019-02-28)
-----------------------
- Optimize attachment query by removing sort and count
  `PR #1578 <https://github.com/onaio/onadata/pull/1578>`_
  [@ukanga]

1.19.1 (2019-02-26)
-----------------------

- Fix TypeError on change_password when format is supplied on URL.
  `PR #1572 <https://github.com/onaio/onadata/pull/1572>`_
  [@bmarika]

1.19.0 (2019-02-21)
-----------------------

- Fix Data Upload Failing
  `Fixes #1561 <https://github.com/onaio/onadata/issues/1561>`_
  [@lincmba]

- Upgrade to pyxform version 0.13.1
  `PR #1570 <https://github.com/onaio/onadata/pull/1570/files>`_
  [@ukanga]

1.18.1 (2019-02-07)
-----------------------

- Pick passed format or default to json in GenericRelatedField serializer
  `PR #1558 <https://github.com/onaio/onadata/pull/1558>`_
  [lincmba]

1.18.0 (2019-01-24)
-----------------------

- Update to pyxform 0.12.2, performance regression fix.
  `Fixes https://github.com/XLSForm/pyxform/issues/247 <https://github.com/XLSForm/pyxform/issues/247>`_
  [ukanga]

- Update projects endpoint API documentation.
  `Fixes #1520 <https://github.com/onaio/onadata/issues/1520>`_
  [lincmba]

- Fix improperly configured URL exception.
  `Fixes #1518 <https://github.com/onaio/onadata/issues/1518>`_
  [lincmba]

- Fix Wrong HTTP method on the project share end point
  `Fixes #1520 <https://github.com/onaio/onadata/issues/1520>`_
  [lincmba]

- Fix files endpoint thumbnail not working for large png images
  `Fixes #1509 <https://github.com/onaio/onadata/issues/1509>`_
  [lincmba]

- Fix recreating the same dataview
  `Fixes #1498 <https://github.com/onaio/onadata/issues/1498>`_
  [lincmba]

- Make sure that when a project is deleted all forms are deleted
  `Fixes #1494 <https://github.com/onaio/onadata/issues/1494>`_
  [bmarika]

- Return better error messages on invalid csv/xls imports
  `Fixes #987 <https://github.com/onaio/onadata/issues/987>`_
  [lincmba]

- Filter media attachments exports
  `Fixes #1028 <https://github.com/onaio/onadata/issues/1028>`_
  [lincmba]

- Remove empty optional fields in formList
  `Fixes #1519 <https://github.com/onaio/onadata/issues/1519>`_
  [lincmba]

- Fix failing bulk csv edits
  `Fixes #1540 <https://github.com/onaio/onadata/issues/1540>`_
  [lincmba]

- Fix TypeError at /api/v1/forms/[pk]/export_async.json
  `Fixes #999 <https://github.com/onaio/onadata/issues/999>`_
  [lincmba]

- Handle DataError during XForms submission
  `Fixes #949 <https://github.com/onaio/onadata/issues/949>`_
  [bmarika]

- Escape apostrophes in SQL queries
  `Fixes #1525 <https://github.com/onaio/onadata/issues/1525>`_
  [bmarika]

- Upgrade kombu
  `PR #1529 <https://github.com/onaio/onadata/pull/1529>`_
  [lincmba]

1.17.0 (2018-12-19)
-------------------

- Fix external Choices with number names
  `Fixes #1485 <https://github.com/onaio/onadata/issues/1485>`_
  [lincmba]

- Remove link expiration message on verification email
  `Fixes #1489 <https://github.com/onaio/onadata/issues/1489>`_
  [lincmba]

- Only generate hash for linked datasets
  `Fixes #1411 <https://github.com/onaio/onadata/issues/1411>`_
  [lincmba]

- Fix merged dataset with deleted parent
  `Fixes #1511 <https://github.com/onaio/onadata/issues/1511>`_
  [lincmba]

- Update/upgrade packages
  `PR 1522 <https://github.com/onaio/onadata/pull/1522>`_
  [lincmba, ukanga]

1.16.0 (2018-12-06)
-------------------

- Fix order extra columns in multiple select exports.
  `Fixes #873 <https://github.com/onaio/onadata/issues/873>`_
  [lincmba]

- Update user roles according to xform meta permissions provided.
  `Fixes #1479 <https://github.com/onaio/onadata/issues/1479>`_
  [lincmba]

- Performance optimisation - use content_type to determine metadata content_object type.
  `Issue #2475 <https://github.com/onaio/onadata/issues/2475>`_
  [ukanga]

- Excel bulk data import support.
  `Issue #1432 <https://github.com/onaio/onadata/issues/1432>`_
  [lincmba]

- Add submission fields to data exports.
  `Issue #1477 <https://github.com/onaio/onadata/issues/1477>`_
  [kahummer]

- Fix error on deleting xform with long id_string or sms_id_string.
  `Issue #1430 <https://github.com/onaio/onadata/issues/1430>`_
  [lincmba]

- Set Default TEMP_TOKEN_EXPIRY_TIME.
  `Issue #1500 <https://github.com/onaio/onadata/issues/1500>`_
  [lincmba]

1.15.0 (2018-10-10)
-------------------

- Submission Reviews
  `Issue #1428 <https://github.com/onaio/onadata/issues/1428>`_
  [DavisRayM, lincmba, moshthepitt]

- Track password edits.
  `Issue #1454 <https://github.com/onaio/onadata/issues/1453>`_
  [lincmba]

1.14.6 (2018-09-03)
-------------------

- Revert Track password edits.
  `Issue #1456 <https://github.com/onaio/onadata/pull/1456>`_
  [lincmba]


1.14.6 (2018-09-03)
-------------------

- Track password edits.
  `Issue #1456 <https://github.com/onaio/onadata/pull/1456>`_
  [lincmba]

- Enable email verification for accounts created via API,
  `Issue #1442 <https://github.com/onaio/onadata/pull/1442>`_
  [ivermac]

- Raise Validation Error when merging forms if there is a PyXFormError
  exception raised.
  `Issue #1153 <https://github.com/onaio/onadata/issues/1153>`_
  [ukanga]

- Update requirements/s3.pip
  `Issue #1465 <https://github.com/onaio/onadata/pull/1465>`_
  [ukanga]


1.14.5 (2018-08-15)
-------------------

- Fix Image resize() function to use file object directly.
  `Issue #1439 <https://github.com/onaio/onadata/pull/1439>`_
  [wambere]

- CSV upload updates
  `Issue #1444 <https://github.com/onaio/onadata/pull/1444>`_
  [ukanga]

- Updated/upgraded packages


1.14.4 (2018-06-21)
-------------------

- Support exporting labels for selects in the data.
  `Issue 1427 <https://github.com/onaio/onadata/issues/1427>`_
  [ukanga]

- Handle UnreadablePostError exception in submissions..
  `Issue 847 <https://github.com/onaio/onadata/issues/847>`_
  [ukanga]

- Support download of CSV XLSForm,
  `Commit 4abd30d <https://github.com/onaio/onadata/commit/4abd30d851512e1e8ab03a350f1869ebcbb4b9bf>`_
  [ukanga]

1.14.3 (2018-05-30)
-------------------

- Support value_select_multiples option in flat CSV, support binary_select_multiples option in API exports.
  `Issue 1409 <https://github.com/onaio/onadata/issues/1409>`_
  [ukanga]

- Check the value of the variable remove when sharing a project with team or
  collaborators, and only remove if value is true
  `Issue 1415 <https://github.com/onaio/onadata/pull/1415>`_
  [wambere]

- Fix TypeError on SPPS Exports with external choices.
  `Issue 1410 <https://github.com/onaio/onadata/issues/1410>`_
  [ukanga]

- Generate XForm hash after every XML change has been applied.
  `Issue 1417 <https://github.com/onaio/onadata/issues/1417>`_
  [ukanga]

- Add api/v1/profiles/[username]/monthly_submissions endpoint.
  `Issue 1423 <https://github.com/onaio/onadata/pull/1423>`_
  [wambere]

- Show metadata only to the owner
  `Issue 1416 <https://github.com/onaio/onadata/issues/1416>`_
  [ukanga]

- Return flow results response timestamp in rfc3339 format explicitly
  `Issue 1420 <https://github.com/onaio/onadata/issues/1420>`_
  [ukanga]

1.14.2 (2018-05-14)
--------------------

- Update check_xform_uuid() to only check for non deleted forms
  `Issue 1403 <https://github.com/onaio/onadata/issues/1403>`_
  [ukanga]

- Persist Flow Results Contact ID and Session ID
  `Issue 1398 <https://github.com/onaio/onadata/pull/1398>`_
  [ukanga]

- Include form version in ODK formList endpoint
  `Issue 1195 <https://github.com/onaio/onadata/issues/1195>`_
  [ukanga]

- Reorder how attachments are saved
  `Issue 961 <https://github.com/onaio/onadata/issues/961>`_
  [wambere]

1.14.1 (2018-05-07)
--------------------

- Fix decimal filter for dataview
  `Issue 1393 <https://github.com/onaio/onadata/pull/1393>`_
  [wambere]

1.14.0 (2018-05-03)
--------------------

- Python 3 support
  `Issue 1295 <https://github.com/onaio/onadata/pull/1295>`_
  [moshthepitt, pld, wambere]

- Add TLS support to messaging
  `Issue 1366 <https://github.com/onaio/onadata/pull/1366>`_
  [ukanga]

- Add date format to submission time filter for forms
  `Issue 1374 <https://github.com/onaio/onadata/pull/1374>`_
  [wambere]

- Update copyright year to 2018
  `Issue 1376 <https://github.com/onaio/onadata/pull/1376>`_
  [pld]

- Catch IOError when saving osm data
  `Issue 1382 <https://github.com/onaio/onadata/pull/1382>`_
  [wambere]

- Remove deleted dataviews from project page
  `Issue 1383 <https://github.com/onaio/onadata/pull/1383>`_
  [wambere]

- Add deleted by field to projects
  `Issue 1384 <https://github.com/onaio/onadata/pull/1384>`_
  [wambere]

- Add check if user has permission to add a project to a profile
  `Issue 1385 <https://github.com/onaio/onadata/pull/1385>`_
  [ukanga]

- Remove note field from csv export appearing in repeat groups
  `Issue 1388 <https://github.com/onaio/onadata/pull/1388>`_
  [wambere]

- Add created by field to cloned forms
  `Issue 1389 <https://github.com/onaio/onadata/pull/1389>`_
  [wambere]

1.13.2 (2018-04-11)
--------------------

- Bump pyxform version to 0.11.1
  `Issue 1355 <https://github.com/onaio/onadata/pull/1355>`_
  [ukanga]

- Update privacy policy to point to hosted privacy policy, tos, and license
  `Issue 1360 <https://github.com/onaio/onadata/pull/1360>`_
  [pld]

- Use resource_name responses for responses endpoint
  `Issue 1362 <https://github.com/onaio/onadata/pull/1362>`_
  [ukanga]



1.13.1 (2018-04-04)
-------------------

- Refactor JSON streaming on data endpoints and removal of X-Total Header
  `Issue 1290 <https://github.com/onaio/onadata/pull/1290>`_
  [wambere]

- Handle Integrity error on creating a project with the same name
  `Issue 928 <https://github.com/onaio/onadata/issues/928>`_
  [wambere]

- Add OSM tags as fields in Excel, SAV/SPSS, CSV zipped exports
  `Issue 1182 <https://github.com/onaio/onadata/issues/1182>`_
  [wambere]

- Delete filtered datasets linked to a form when deleting a form
  `Issue 964 <https://github.com/onaio/onadata/issues/964>`_
  [wambere]

- Add timestamp to Messaging
  `Issue 1332 <https://github.com/onaio/onadata/issues/1332>`_
  [moshthepitt]

- Update messaging schema for forms to include metadata of the form.
  `Issue 1331 <https://github.com/onaio/onadata/issues/1331>`_
  [moshthepitt]

- Improve setup.py and dependency management
  `Issue 1330 <https://github.com/onaio/onadata/issues/1330>`_
  [moshthepitt]
