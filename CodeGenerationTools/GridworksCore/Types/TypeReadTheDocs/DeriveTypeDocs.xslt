<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:msxsl="urn:schemas-microsoft-com:xslt" exclude-result-prefixes="msxsl" xmlns:xs="http://www.w3.org/2001/XMLSchema">
    <xsl:output method="xml" indent="yes" />
    <xsl:param name="root" />
    <xsl:param name="codee-root" />
    <xsl:include href="../CommonXsltTemplates.xslt"/>
    <xsl:param name="exclude-collections" select="'false'" />
    <xsl:param name="relationship-suffix" select="''" />
    <xsl:variable name="airtable" select="/" />
    <xsl:variable name="squot">'</xsl:variable>
    <xsl:variable name="init-space">
    </xsl:variable>
    <xsl:variable name="colon">:</xsl:variable>
    <xsl:include href="GnfCommon.xslt"/>

    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()" />
        </xsl:copy>
    </xsl:template>

    <xsl:template match="/">
        <FileSet>

            <FileSetFile>
                    <xsl:element name="RelativePath"><xsl:text>../../../../docs/schemata.rst</xsl:text></xsl:element>

                <OverwriteMode>Never</OverwriteMode>
                <xsl:element name="FileContents">
<xsl:text>
GridWorks Atn Schemata
============

.. automodule:: gwatn.schemata
</xsl:text>
<xsl:for-each select="$airtable//ProtocolTypes/ProtocolType[(normalize-space(ProtocolName) ='atn')]">
<xsl:sort select="TypeName" data-type="text"/>
<xsl:variable name="schema-id" select="Type"/>
<xsl:for-each select="$airtable//Schemas/Schema[(SchemaId = $schema-id)  and (Status = 'Active' or Status = 'Pending') and (ProtocolCategory = 'Json' or ProtocolCategory = 'GwAlgoSerial')]">
<xsl:variable name="local-alias" select="AliasRoot" />

<xsl:text>
.. automodule</xsl:text>
   <xsl:value-of select="$colon"/>
   <xsl:value-of select="$colon"/><xsl:text> gwatn.schemata.</xsl:text>
        <xsl:value-of select="translate(AliasRoot,'.','_')" />
    <xsl:value-of select="$init-space"/>
    <xsl:value-of select="$colon"/>
    <xsl:text>
    members

.. autoclass</xsl:text>
       <xsl:value-of select="$colon"/>
   <xsl:value-of select="$colon"/><xsl:text> </xsl:text>
   <xsl:call-template name="nt-case">
    <xsl:with-param name="mp-schema-text" select="AliasRoot" />
</xsl:call-template>
  <xsl:text>
    members

</xsl:text>

</xsl:for-each>
</xsl:for-each>




                </xsl:element>
            </FileSetFile>


        </FileSet>
    </xsl:template>


</xsl:stylesheet>
